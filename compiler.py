from ast import *
from compilertools import *
from parser import Parser
import os # might need this for sys args?
from Graph import *
import threading
import queue

variables = []
pre_allocations = {}
MODULES_PATH = "./modules/"

def flatten_dependencies(file_tree, namespace, dep_map):
    f = Flattener(file_tree, namespace, dep_map) # frontend

    #print(ast.dump(file_tree, indent=4))
        
    return file_tree, namespace, f.free_vars, f.top_level_assignments, f.getVariables()

def compile_to_ir(file_tree, dep_trees, dep_map, all_variables):
    
    #f = Flattener(file_tree, "", dep_map)
    #print(ast.dump(file_tree, indent=4))
    
    combined_deps = []

    for dep_tree in dep_trees:
        combined_deps += dep_tree.body

    file_tree.body = combined_deps + file_tree.body
     
    open(f"debug/ast_post_combine.py", "w").write(ast.dump(file_tree, indent=4))
    open(f"debug/post_combine.py", "w").write(ast.unparse(file_tree))
    
    funcs, curr_lbl = func_create(file_tree, 0)

    #print(funcs)
    
    func_ir = []
    func_names = set()
    variables = list(all_variables)
    
    for i, func in enumerate(funcs):
        new_graph = Graph([])
        func_ir.append(create_ir_graph(func, new_graph, True))
        func_names.add(func_ir[i].vertices[0].value[:-1])
    
    ir, curr_lbl = convert_to_ir(file_tree, curr_lbl)
    #pretty_print(ir)
    ir_graph = create_ir_graph(ir, Graph([]), False)
    #print(ir_graph)
    

    reg_dict = {f"%eax": 0, f"%ecx": 1, f"%edx": 2, f"%edi": 3, f"%ebx": 4, f"%esi": 5}

    caller_reg_dict = {f"%eax": 0, f"%ecx": 1, f"%edx": 2}
    
    thread_val_tuples = []

    # start threads
    for i, graph in enumerate(func_ir):
        q = queue.Queue()
        t = threading.Thread(target=assign_regs, args=(graph, funcs[i], variables.copy(), caller_reg_dict.copy(), q))
        print("started thread: ", i)
        t.start()
        thread_val_tuples.append((t, q))

    inter_graphs = [assign_regs(ir_graph, file_tree, variables.copy(), reg_dict.copy())]
  
    # join threads
    for i, graph in enumerate(func_ir):
        thread_val_tuples[i][0].join()
        inter_graphs.append(thread_val_tuples[i][1].get_nowait())
        print("joined thread: ", i)
        func_ir[i].vertices[0].block = [["pushl %ebp"], ["movl %esp, %ebp"], ['set_stack']] + func_ir[i].vertices[0].block
        func_ir[i].vertices[-1].block += [["movl %ebp, %esp"], ["popl %ebp"], ["ret"]]
    

    ir_graph.vertices[0].block = [[".globl main"], ["main:"], ["pushl %ebp"], ["movl %esp, %ebp"], ["set_stack"]] + ir_graph.vertices[0].block
    ir_graph.vertices[-1].block += [["movl $0, %eax"], ["leave"], ["ret"]]

    assembly = generate_assembly([ir_graph] + func_ir, inter_graphs, func_names)
    
    return assembly
    
def generate_assembly(ir_graphs, inter_graphs, func_names):
    assembly = f""

    for graph1, graph2 in zip(ir_graphs, inter_graphs):
        ir_graph = graph1
        graph, stack_size = graph2
        split_graph = ir_graph.vertices[0].value.split('.')
        if split_graph[-1][0] == 't':
            assembly += f"{ir_graph.vertices[0].value}\n"
        for ir_node in ir_graph.vertices:
            split_node = ir_node.value.split('.')
            if split_node[-1][0] != 't' and ir_node.value != 'start':
                assembly += f"{ir_node.value}:\n"
            for i, ins in enumerate(ir_node.block):
                if (ins[0] == "call"):
                    if (ins[1] == "eval_input"):
                        assembly += f"{ins[0]} eval_input_pyobj"
                    else:
                        for var in reversed(ins[2:]):
                            if (var in graph):  
                                if (var in func_names):
                                    assembly += f"movl ${var}, {graph[var]['color']}\n"
                                
                                assembly += f"pushl {graph[var]['color']}\n"
                            else:
                                assembly += f"pushl ${var}\n"

                        if (ins[1] == "print"):
                            assembly += f"{ins[0]} print_any"
                        elif ins[1] in graph:
                            assembly += f"{ins[0]} *{graph[ins[1]]['color']}"
                        else:
                            assembly += f"{ins[0]} {ins[1]}"

                        assembly += f"\naddl ${4 * len(ins[2:])}, %esp"
                elif (ins[0] == "negl"):
                    if (ins[1] in graph):  
                        assembly += f"{ins[0]} {graph[ins[1]]['color']}"
                    else:
                        assembly += f"{ins[0]} ${ins[1]}"
                elif (ins[0] == "movl" or ins[0] == "addl" or ins[0] == "cmpl"):
                    if (ins[2] in graph):
                        if (i >= 1 and ir_node.block[i - 1][0] == "call" and ir_node.block[i - 1][1] != "print" and ir_node.block[i - 1][1] != "set_subscript"):
                            assembly += f"{ins[0]} %eax, {graph[ins[2]]['color']}"
                        elif (ins[1] in graph):  
                            assembly += f"{ins[0]} {graph[ins[1]]['color']}, {graph[ins[2]]['color']}"
                        elif (str(ins[1])[-1] == ')'):  
                            assembly += f"{ins[0]} {ins[1]}, {graph[ins[2]]['color']}"
                        else:
                            assembly += f"{ins[0]} ${ins[1]}, {graph[ins[2]]['color']}"
                    else:
                        if (ins[1] in graph):  
                            assembly += f"{ins[0]} {graph[ins[1]]['color']}, ${ins[2]}"
                        else:
                            assembly += f"{ins[0]} ${ins[1]}, ${ins[2]}"
                elif ins[0] == "movzbl":
                    assembly += f"{ins[0]} %al, {graph[ins[2]]['color']}"
                elif ins[0] == "set_stack":
                    assembly += f"subl ${stack_size * 4}, %esp"
                elif ins[0] == "reset_stack":
                    assembly += f"addl ${stack_size * 4}, %esp"
                elif ins[0] == "ret" and len(ins) == 2 and ins[1] in graph:
                    assembly += f"movl {graph[ins[1]]['color']}, %eax"
                else:
                    for val in ins:
                        assembly += f"{val} "
                assembly += "\n"
         # pop stack # TODO: update the pop x amount depending on args? 
    return assembly

def assign_regs(ir_graph, file_tree, var_assignments, reg_dict, q = None):
    #print(var_assignments)
    calle_reg_set = {f"%eax", f"%ecx", f"%edx"}
    
    tmp_counter = 0
    stack_counter = 1
    temp_var_name = "tmp"
    pre_allocated_vars = list(pre_allocations.keys())

    # we don't use this but keeping it around for future
    def add_callee_liveness(name, op):
        r_k = set()
        if (op == 'call'):
            r_k.update(calle_reg_set)
        return r_k

    def add_callee_saved_regs(inter_graph, name, op):
        nodes = set()
        if (op == 'call'):
            for i, reg in enumerate(calle_reg_set):
                node = name + str(i)
                nodes.add(node)
                if not (node in inter_graph):
                    inter_graph[node] = {'edges': set(), 'color': reg, 'spill_indices': [], 'should_spill': False}
        if (name == f'%al'):
            nodes.add("al")
            if not ("al" in inter_graph):
                inter_graph["al"] = {'edges': set(), 'color': f'%eax', 'spill_indices': [], 'should_spill': False}
        return nodes

    def isVarPreallocated(var_name):
        for name in pre_allocated_vars:
            if name in var_name:
                return True

        return False

    def calc_liveness(node, live_vars, inter_graph):
        #print('liveness')
        if (not len(node.liveness)):
            node.liveness = [set() for i in range(len(node.block) + 1)]

        if (len(node.liveness)):
            node.liveness[0].update(live_vars)
            node.collected += 1

        #print(node.value, node.liveness[0], node.collected, len(node.directedTo))

        liveness_changed = False

        collection_size = len(node.directedTo)

        if ('while' in node.value):
            collection_size = sum('loop' not in sub_node.value for sub_node in node.directedTo)
            #print(node.value, collection_size)

        if (node.collected >= collection_size):
            node.collected = 0
            for i, ins in enumerate(node.block[::-1]): # iterate backwards over ir
                w_k = set()
                r_k = set()
                reverse_i = len(node.block) - 1 - i
                if ins[0] == 'movl':
                    if ins[1] in var_assignments: # reading from var
                        r_k.add(ins[1])
                        if not (temp_var_name in ins[1]) and [node, reverse_i] not in inter_graph[ins[1]]['spill_indices']:
                            inter_graph[ins[1]]['spill_indices'].append([node, reverse_i])
                    if ins[2] in var_assignments: # technically not needed since movl always write to var
                        w_k.add(ins[2])
                        if not (temp_var_name in ins[2]) and [node, reverse_i] not in inter_graph[ins[2]]['spill_indices']:
                            inter_graph[ins[2]]['spill_indices'].append([node, reverse_i])
                            if (isVarPreallocated(ins[1])):
                                inter_graph[ins[2]]['should_spill'] = True
                elif ins[0] == 'movzbl':
                    if ins[2] in var_assignments:
                        w_k.add(ins[2])
                        if not (temp_var_name in ins[2]) and [node, reverse_i] not in inter_graph[ins[2]]['spill_indices']:
                            inter_graph[ins[2]]['spill_indices'].append([node, reverse_i])
                            inter_graph[ins[2]]['should_spill'] = True
                elif ins[0] == 'addl':
                    if ins[1] in var_assignments: # reading from var
                        r_k.add(ins[1])
                        if not (temp_var_name in ins[1]) and [node, reverse_i] not in inter_graph[ins[1]]['spill_indices']:
                            inter_graph[ins[1]]['spill_indices'].append([node, reverse_i])
                            inter_graph[ins[1]]['should_spill'] = True
                    if ins[2] in var_assignments: # technically not needed since movl always write to var
                        r_k.add(ins[2])
                        w_k.add(ins[2])
                elif ins[0] == 'cmpl':
                    if ins[1] in var_assignments: # reading from var
                        r_k.add(ins[1])
                        if not (temp_var_name in ins[1]) and [node, reverse_i] not in inter_graph[ins[1]]['spill_indices']:
                            inter_graph[ins[1]]['spill_indices'].append([node, reverse_i])
                            inter_graph[ins[1]]['should_spill'] = True
                    if ins[2] in var_assignments: # technically not needed since movl always write to var
                        r_k.add(ins[2])
                elif ins[0] == 'negl':
                    if ins[1] in var_assignments:
                        r_k.add(ins[1])
                        if not (temp_var_name in ins[1]) and [node, reverse_i] not in inter_graph[ins[1]]['spill_indices']:
                            inter_graph[ins[1]]['spill_indices'].append([node, reverse_i])
                            inter_graph[ins[1]]['should_spill'] = True
                        w_k.add(ins[1])
                elif ins[0] == 'call':
                    for var in ins[1:]:
                        if var in var_assignments:
                            r_k.add(var)
                elif ins[0] == 'ret' and len(ins) > 1:
                    if ins[1] in var_assignments: # reading from var
                        r_k.add(ins[1])
                # print(node.value, i + 1, node.liveness[i], w_k, r_k)

                old_set = node.liveness[i + 1].copy()
                node.liveness[i + 1].update(node.liveness[i].difference(w_k).union(r_k))
                if (len(node.liveness[i + 1]) != len(old_set)):
                    liveness_changed = True
                # print(node.value, i + 1, node.liveness[i + 1])

            for next_node in node.directedFrom:
                if ('while' in node.value):
                    #print(liveness_changed, next_node.value)
                    if not liveness_changed and not ('loop' + node.value[5] in next_node.value or 'en' in next_node.value):
                        calc_liveness(next_node, node.liveness[-1], inter_graph)
                    elif liveness_changed and ('loop' + node.value[5] in next_node.value or 'en' in next_node.value):
                        calc_liveness(next_node, node.liveness[-1], inter_graph)
                else:
                    calc_liveness(next_node, node.liveness[-1], inter_graph)

    def reset_liveness(ir_graph):
         for node in ir_graph.vertices:
            node.collected = 0
            node.liveness.clear()

    def clean_liveness(ir_graph):
        for node in ir_graph.vertices:
            if (len(node.liveness)):
                node.liveness.reverse()

    def generate_inter_graph(ir_graph, inter_graph):
        for ir_node in ir_graph.vertices:
            for ins in range(len(ir_node.block)): # generate interference graph
                l_k = ir_node.liveness[ins+1]
                if ir_node.block[ins][0] == 'movl' or ir_node.block[ins][0] == 'movzbl' or ir_node.block[ins][0] == 'call':
                    l_k.update(add_callee_saved_regs(inter_graph, ir_node.block[ins][1], ir_node.block[ins][0]))
                    l_k.discard(ir_node.block[ins][1])
                    for node in l_k:
                        #print('edge updates')     
                        inter_graph[node]['edges'].update(l_k.difference({node}))
                else:
                    for node in l_k:
                        #print('edge updates')     
                        inter_graph[node]['edges'].update(l_k.difference({node}))

    shouldRepeat = True
    reg_count = len(reg_dict)

    while(shouldRepeat): # repeat process until spill vars are all covered
        inter_graph = {key: {'edges': set(), 'color': None, 'spill_indices': [], 'should_spill': False} for key in var_assignments} # convert list of vars to graph # liveness between each innstruction
        for key in pre_allocations.keys():
            if key in inter_graph:
                inter_graph[key]['color'] = pre_allocations[key]
                

        shouldRepeat = False

        reset_liveness(ir_graph)
        calc_liveness(ir_graph.vertices[-1], set(), inter_graph)
        clean_liveness(ir_graph)
        #print(ir_graph)

        generate_inter_graph(ir_graph, inter_graph)

        color_order = sorted([(key, val) for key, val in inter_graph.items()], key=lambda node: (int(temp_var_name in node[0]) * len(inter_graph)) + len(node[1]['edges']), reverse=True)

        for node in color_order: 
            if (node[1]['color'] == None):
                color_options = reg_dict.copy()
                for edge in node[1]['edges']:
                    #print(edge)
                    color_options.pop(inter_graph[edge]['color'], None)

                new_reg = ""
                if (len(color_options)): # successful color
                    new_reg = next(iter(color_options))
                    node[1]['color'] = new_reg
                    if not ("ebp" in new_reg):
                        continue
                else:  # spill code   
                    new_reg = f"{stack_counter * -4}(%ebp)"
                    reg_dict[new_reg] = stack_counter + reg_count
                    stack_counter += 1
                    #print(stack_counter)
                    reg_count = len(reg_dict)

                node[1]['color'] = new_reg
                spill_indices_temp = node[1]['spill_indices']

                spill_indices = []
                [spill_indices.append(x) for x in spill_indices_temp if x not in spill_indices]

                if (node[1]['should_spill']):
                    shouldRepeat = True
                    #print(node[0], spill_indices)
                    #print(spill_indices)      
                    for ir_node, i in spill_indices:   
                        new_var = temp_var_name + str(tmp_counter)
                        var_assignments.append(new_var)
                        tmp_counter += 1
                        if ir_node.block[i][0] == 'movzbl' or (ir_node.block[i][0] == 'movl' and ir_node.block[i][2] == node[0]):
                            ir_node.block[i][2] = new_var
                            ir_node.block.insert(i + 1, ['movl', new_var, node[0]])
                        else:
                            ir_node.block.insert(i, ['movl', node[0], new_var])

                            if (ir_node.block[i + 1][0] == 'call' and ir_node.block[i + 1][1] != 'eval_input'):
                                for j, var in enumerate(ir_node.block[i + 1][2:]):
                                    if var == node[0]:
                                        ir_node.block[i + 1][j] = new_var
                                        break
                            else:
                                ir_node.block[i + 1][1] = new_var

                        for j, spill_tuple in enumerate(spill_indices[i:]):
                            if spill_tuple[0].value == ir_node.value and spill_tuple[1] > i:
                                spill_tuple[1] += 1
                    break
                else:
                    for ir_node, i in spill_indices:
                        #print('spill checks')
                        if (ir_node.block[i][0] == 'movl'):
                            if (ir_node.block[i][1] == node[0] and ir_node.block[i][2] in inter_graph):
                                inter_graph[ir_node.block[i][2]]['should_spill'] = True
                            elif (ir_node.block[i][1] in inter_graph):
                                inter_graph[ir_node.block[i][1]]['should_spill'] = True

    #print(ir_graph)

    #for key, value in inter_graph.items():
        #print(f"Var: {key}, Reg: {value['color']}, Edges: {value['edges']}")

    print("stack_counter", stack_counter)

    if (q):
        q.put_nowait((inter_graph, stack_counter - 1))

    return inter_graph, stack_counter - 1

def func_create(file_tree: AST, start_lbl) -> list:
    func_lst = []
    for node in file_tree.body.copy():
        if isinstance(node, FunctionDef):
            ir, start_lbl = convert_to_ir(Module([node]), start_lbl)
            func_lst.append(ir)
            file_tree.body.remove(node)
    return func_lst, start_lbl

def convert_to_ir(file_tree: AST, jmp_lbl = 0): # labels to keep track of if/while gotos
    ir = []

    ops = {USub: 'negl', Add: 'addl', Eq: 'sete', NotEq: 'setne'} # add to this as needed in the future
    for node in file_tree.body:
        if isinstance(node, Assign): # assigning of variable
            value = node.value
            var_id = node.targets[0].id

            if isinstance(value, Constant): # assigning to const
                ir.append(['movl', value.value, var_id])
            elif isinstance(value, UnaryOp): #assigning to unary op
                if isinstance(value.operand, Name):
                    ir.append(['movl', value.operand.id, var_id])
                elif isinstance(value.operand, Constant):
                    ir.append(['movl', value.operand.value, var_id])
                ir.append([ops[value.op.__class__], var_id])
            elif isinstance(value, BinOp): # assigning to binary op
                first = value.left
                second = value.right

                if (isinstance(value.right, Name) and value.right.id == var_id):
                    first = value.right
                    second = value.left
                if (isinstance(first, Name)):
                    if (first.id != var_id):
                        ir.append(['movl', first.id, var_id])
                else:
                    ir.append(['movl', first.value, var_id])

                if (isinstance(second, Name)):
                    ir.append([ops[value.op.__class__], second.id, var_id])
                else:
                    ir.append([ops[value.op.__class__], second.value, var_id])
            elif isinstance(value, Call): # assign to eval
                if value.func.id == 'eval':
                    ir.append(['call', 'eval_input'])
                    ir.append(['movl', 'eval_input', var_id])
                elif value.func.id == 'print': # edge case
                    #print('invalid syntax assign to func')
                    os.error(NotImplementedError)
                    os.sys.exit(-1)
                else:
                    call_ir = ['call', value.func.id]
                    for arg in value.args:
                        if (isinstance(arg, Name)):
                            call_ir.append(arg.id)
                        elif (isinstance(arg, Constant)):
                            call_ir.append(arg.value)
                    ir.append(call_ir)
                    ir.append(['movl', value.func.id, var_id])
                    
            elif isinstance(value, Name): # setting var equal to var
                ir.append(['movl', value.id, node.targets[0].id])
            elif isinstance(value, Compare): # == and !=
                left = value.left
                comparator = value.comparators[0] # TODO: account for mult in future?

                if isinstance(left, Name) and isinstance(comparator, Constant):
                    left = comparator.value
                    comparator = value.left.id
                else:
                    left = left.id if isinstance(left, Name) else left.value 
                    comparator = comparator.id if isinstance(comparator, Name) \
                        else comparator.value

                ir.append(['cmpl', left, comparator])
                ir.append([ops[value.ops[0].__class__], "%al"])
                ir.append(['movzbl', '%al', var_id])
            else: # ignore all other cases
                #print(f'invalid syntax for assign')
                os.error(NotImplementedError)
                os.sys.exit(-1)
        elif isinstance(node, Expr): # calling of function (print and eval)
            expr = node.value
            # push val to stack
            if isinstance(expr, Call):
                if expr.func.id == 'print': # func is print
                    args = expr.args
                    if isinstance(args[0], Name): # TODO: iterate over all args (maybe?)
                        ir.append(['call', 'print', args[0].id])
                    else: # const
                        ir.append(['call', 'print', args[0].value])
                else:
                    call_ir = ['call', expr.func.id]
                    for arg in expr.args:
                        if (isinstance(arg, Name)):
                            call_ir.append(arg.id)
                        elif (isinstance(arg, Constant)):
                            call_ir.append(arg.value)
                    ir.append(call_ir)
            else:
                continue
        elif isinstance(node, If): # if statement
            test = node.test
            body = node.body
            orelse = node.orelse
            curr_lbl = jmp_lbl

            test = test.id if isinstance(test, Name) else test.value
            ir.append(['cmpl', 0, test]) # if test
            jump = f"else{curr_lbl}" if orelse else f"enif{curr_lbl}"
            ir.append(['je', jump])
            ir.append(f"then{curr_lbl}:")

            # if body
            body_ir, jmp_lbl = convert_to_ir(Module(body), jmp_lbl=jmp_lbl+1)
            ir += body_ir
            ir.append(['jmp', f"enif{curr_lbl}"])

            if orelse: # or else
                ir.append(f"else{curr_lbl}:")
                orelse_ir, jmp_lbl = convert_to_ir(Module(orelse), jmp_lbl=jmp_lbl+1)
                ir += orelse_ir

            ir.append(f"enif{curr_lbl}:")
            jmp_lbl += 1
        elif isinstance(node, While): # raw ducking pain
            test = node.test 
            body = node.body
            curr_lbl = jmp_lbl

            test = test.id if isinstance(test, Name) else test.value
            ir.append(f"while{curr_lbl}:")
            ir.append(['cmpl', 0, test]) # if test
            ir.append(['je', f"end{curr_lbl}"])

            # while body
            ir.append(f"loop{curr_lbl}:")
            body, jmp_lbl = convert_to_ir(Module(body), jmp_lbl=jmp_lbl+1)
            ir += body
            ir.append(['jmp', f"while{curr_lbl}"])

            ir.append(f"end{curr_lbl}:")
            jmp_lbl +=1
        elif isinstance(node, FunctionDef):
            ir.append(f"{node.name}:")
            for i, arg in enumerate(node.args.args):
                num = str(len(pre_allocations.keys()))
                variables.append(arg.arg)
                pre_allocations[arg.arg] = f"{(i + 2) * 4}(%ebp)"
            body, jmp_lbl = convert_to_ir(Module(node.body), jmp_lbl=jmp_lbl)
            ir += body
        elif isinstance(node, Return):
            val = node.value.id if isinstance(node.value, Name) else node.value.value
            ir.append(['ret', val])
        else: # ignore all other cases
            print(f'invalid syntax for {node}')
            #os.error(NotImplementedError)
            #os.sys.exit(-1)
    return ir, jmp_lbl

def create_ir_graph(ir, graph, is_func = False) -> Graph:
    curr_block = []
    labels = []
    if is_func:
        labels = [ir[0]]
        del ir[0]
    else:
        labels = ["start"]
    blocks = []

    for ins in ir:
        if isinstance(ins, list):
            curr_block.append(ins)
        else:
            labels.append(ins[:-1])
            blocks.append(curr_block)
            curr_block = []
    blocks.append(curr_block)
    
    block_map = {lbl: blk for lbl, blk in zip(labels, blocks)}
    for lbl in block_map: # create initial graph
        graph.addVertex(v=lbl, block=block_map[lbl])

    if len(graph.vertices) > 1:
        index = len(graph.vertices)-1
        for v in graph.vertices[::-1]: # add edges
            if index-1 >= 0:
                prev_node = graph.vertices[index-1]
                # print(prev_node)
                if "else" not in v.value and "end" not in v.value: # god forbid I have fun
                    graph.addDirectedEdge(prev_node.value, v.value)
            for vert in graph.vertices:
                if len(vert.block) and v.value in vert.block[-1]:
                    graph.addDirectedEdge(vert.value, v.value)
            index -= 1
    return graph

def pretty_print(ir): # prints ir but pretty
    print("[")
    for ins in ir:
        if isinstance(ins, list):
            if ins[0] != 'ret':
                print(f"\t{ins}")
            else: # ret
                print(f"\t{ins}")
                print("    ------------------------")
        else:
            print("    ------------------------")
            print(f"    {ins}")
    print("]")

def compile(file, namespace = "", directory = "", q = None):
    file_trees = []
    dep_map = {}
    all_variables = set()

    dependency_files = []
    with open(file) as f:
        for line in f:
            broken_line = line.split(" ")
            if (len(broken_line) == 4 and broken_line[0] == "#import"):
                dependency_files.append((directory + broken_line[1][1:-1], broken_line[3][:-1]))
            else:
                break
        
        f.close()
    
    #print(dependency_files)
    
    thread_val_tuples = []

    # start threads
    for i, (dep_file, dep_namespace) in enumerate(dependency_files):
        if (namespace):
            new_namespace = namespace + "." + dep_namespace
        else:
            new_namespace = dep_namespace

        new_q = queue.Queue()
        t = threading.Thread(target=compile, args=(dep_file, new_namespace, dep_file[0:dep_file.rfind('/') + 1], new_q))
        print("started file thread: ", i)
        t.start()
        thread_val_tuples.append((t, new_q))
  
    # join threads
    for i, deps in enumerate(dependency_files):
        thread_val_tuples[i][0].join()

        new_file_trees, new_dep_map, new_vars = thread_val_tuples[i][1].get_nowait()
        file_trees += new_file_trees
        dep_map.update(new_dep_map)
        all_variables.update(new_vars)
        print("joined file thread: ", i)
        
    with open(file) as f:
        file_to_compile = f.read()
        file_tree = ast.parse(file_to_compile)
        
        file_tree, namespace, free_vars, var_mappings, new_vars = flatten_dependencies(file_tree, namespace, dep_map)

        dep_map[namespace] = (free_vars, var_mappings)
        all_variables.update(new_vars)
        file_trees.append(file_tree)

        f.close()

    if (q):
        q.put_nowait((file_trees, dep_map, all_variables))

    return file_trees, dep_map, all_variables

def compile_outer(file):
    file_trees, dep_map, all_variables = compile(file)

    assembly = compile_to_ir(file_trees[-1], file_trees[:-1], dep_map, all_variables)

    binary_file = open(f"{os.path.splitext(file)[0]}.s", "w") # create .s file
    binary_file.write(assembly)

def compile_n_files(files):
    # start threads
    threads = []
    for file in files:
        with open(file) as f: # check file exists
            if f.closed:
                print("file does not exist")
                os.sys.exit(-1)

        t = threading.Thread(target=compile_outer, args=(file, ))
        print(f"started thread {t}")
        t.start()
        threads.append(t)

    for thread in threads: # join threads
        thread.join()


def check_dependencies(file_tree, files):
    for child_node in ast.iter_child_nodes(file_tree):
        if isinstance(child_node, Import):
            for alias in child_node.names:
                if ((alias.name + ".py") not in files):
                    sys.exit("File dependency does not exist or was not passed")


if __name__ == "__main__":
    if len(os.sys.argv) < 2:
        print("Usage: compiler.py <file1> <file2> ...")
        os.sys.exit(-1)

    compile_n_files(os.sys.argv[1:])
    # compile_outer(os.sys.argv[1])