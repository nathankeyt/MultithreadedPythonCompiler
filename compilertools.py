import ast 
from ast import *

unary_explicate_types = {'USub', 'Not'}
binary_explicate_types = {'Add', 'And', 'Or', 'Eq', 'NotEq', 'Is'}
built_in_names = {'print', 'int', 'set_free_vars' 'bool', 'list', 'dict', 'create_closure', 'create_list', 'get_free_vars', 'is_int', 'is_bool', 'is_big', 'is_true', 'inject_int', 'project_int', 'inject_bool', 'project_bool', 'inject_big', 'project_big', 'set_subscript', 'get_subscript', 'throw_type_error', 'add', 'equal', 'not_equal', 'eval_input', 
'eval', 'input', 'create_dict'}

class Flattener():
    def __init__(self, n: AST, namespace="", dep_map={}, debug=True):
        self.root = n # create new tree
        self.var_count = 0
        self.pre_assignments = {}
        self.funcs_to_frees = {}
        self.free_vars = set()
        self.shouldInject = True
        self.free_var_count = 0
        self.crossed_off_vars = set()
        self.funcs_to_free_count = {}
        self.top_level_assignments = {}
        self.dep_map = dep_map
        self.dep_vars = set()
        self.dep_free_vars = set()
        self.namespace = namespace
        
        if (namespace):
            self.var_title = namespace + '.t'
        else:
            self.var_title = 't'

        for free_vars, var_mappings in dep_map.values():
            self.free_vars.update(free_vars)
            self.dep_free_vars.update(free_vars)
        
            for var in var_mappings.values():
                self.dep_vars.add(var)

        if debug:
            open(f"debug/ast_original.py", "w").write(ast.dump(n, indent=4))
            #print("initialized flattener")

        self.unify_defs(n, [0])
        self.top_level_assignments = self.uniqify(n, {})[0]
        ast.fix_missing_locations(n)

        if debug:
            open(f"debug/ast_post_uniqify.py", "w").write(ast.dump(n, indent=4))
            open(f"debug/post_uniqify.py", "w").write(ast.unparse(n))

        #sys.exit("exit at uniq")

        self.get_free_vars(self.free_vars, n)
        self.heapify(n, self.free_vars, set())
        ast.fix_missing_locations(n)

        if debug:
            open(f"debug/ast_post_heapify.py", "w").write(ast.dump(n, indent=4))
            open(f"debug/post_heapify.py", "w").write(ast.unparse(n))
        
        self.closure_convert(n)
        ast.fix_missing_locations(n)

        if debug:
            open(f"debug/ast_pre_flat.py", "w").write(ast.dump(n, indent=4))
            open(f"debug/pre_flat.py", "w").write(ast.unparse(n))
            #print("Passed: unify_defs, uniqify, heapify, closure_convert")

        self.flatten(n)
        ast.fix_missing_locations(n)

        if debug:
            open(f"debug/ast_post_flat.py", "w").write(ast.dump(n, indent=4))
            open(f"debug/post_flat.py", "w").write(ast.unparse(n))
            #print("passed flatten")

        self.explicate_pass(n)
        #self.uniqify(n)
        ast.fix_missing_locations(n)

        if debug:
            open(f"debug/ast_post_explicate.py", "w").write(ast.dump(n, indent=4))
            open(f"debug/post_explicate.py", "w").write(ast.unparse(n))
            #print("passed explicate")

    def access_dict_ns(self, dic, key):
        if (self.namespace):
            key = self.namespace + '.' + key
        #print(dic)
        if key in dic:
            #print(dic[key])
            return dic[key]
        
        return None

    def in_dict_ns(self, dic, key):
        if (self.namespace):
            key = self.namespace + '.' + key

        return key in dic

    def flatten(self, n, parent = [], body_index = 0, shouldFlatten = False):
        if isinstance(n, Module):
            self.root = n
            #self.var_count = 0
            #self.pre_assignments.clear()

            for node in n.body.copy():
                body_index = self.flatten(node, n.body, body_index)[1]
                body_index += 1

            n = ast.fix_missing_locations(n)

            return (n, body_index)
        elif isinstance(n, Subscript):
            n.value, body_index = self.flatten(n.value, parent, body_index, True)
            n.slice, body_index = self.flatten(n.slice, parent, body_index, True)
                    
            return self.flattenNode(n, parent, body_index, True)
        elif isinstance(n, Assign):
            n.value, body_index = self.flatten(n.value, parent, body_index)

            if isinstance(n.targets[0], Subscript):
                n.targets[0].slice, body_index = self.flatten(n.targets[0].slice, parent, body_index, True)
                n.targets[0].value, body_index = self.flatten(n.targets[0].value, parent, body_index, True)
                n.value, body_index = self.flattenNode(n.value, parent, body_index, True)
                
                    
            return (n, body_index)
        elif isinstance(n, Constant):
            if (self.shouldInject):
                if isinstance(n.value, bool):
                    return self.flattenNode(Call(Name('inject_bool', Load()), [Constant(int(n.value))], []), parent, body_index, shouldFlatten)
                else:
                    return self.flattenNode(Call(Name('inject_int', Load()), [n], []), parent, body_index, shouldFlatten)
            else:
                return (n, body_index)
        elif isinstance(n, List):
            for i, element in enumerate(n.elts):
                if isinstance(element, Name):
                    n.elts[i], body_index = self.flattenNode(element, parent, body_index, True)
                else:
                    n.elts[i], body_index = self.flatten(element, parent, body_index, True)

            return self.flattenNode(n, parent, body_index, shouldFlatten)
        elif isinstance(n, Dict):
            for i, element in enumerate(n.keys):
                n.keys[i], body_index = self.flatten(element, parent, body_index, True)

            for i, element in enumerate(n.values):
                n.values[i], body_index = self.flatten(element, parent, body_index, True)

            return self.flattenNode(n, parent, body_index, shouldFlatten)
        elif isinstance(n, BinOp):
            n.left, body_index = self.flatten(n.left, parent, body_index, True)
            n.right, body_index = self.flatten(n.right, parent, body_index, True)

            return self.flattenNode(n, parent, body_index, shouldFlatten)
        elif isinstance(n, Compare):
            nextConstFlatten = False
            if isinstance(n.left, Constant):
                nextConstFlatten = True

            n.left, body_index = self.flatten(n.left, parent, body_index, True)
  
            for index, comparator in enumerate(n.comparators):
                if isinstance(comparator, Constant) and nextConstFlatten:
                    n.comparators[index], body_index = self.flattenNode(comparator, parent, body_index, True)
                else:
                    n.comparators[index], body_index = self.flatten(comparator, parent, body_index, True)

            return self.flattenNode(n, parent, body_index, shouldFlatten)
        elif isinstance(n, BoolOp):
            n.values[0], body_index = self.flatten(n.values[0], parent, body_index, True)
            n.values[1], body_index = self.flatten(n.values[1], parent, body_index, True)

            #if (isinstance(n.op, And)):
                #n = ast.copy_location(IfExp(n.values[0], n.values[1], Constant(0)), n)
            #elif (isinstance(n.op, Or)):
                #n = ast.copy_location(IfExp(n.values[0], Constant(1), n.values[1]), n)
            #else:
                #return (n, body_index)

            return self.flattenNode(n, parent, body_index, shouldFlatten)
        elif isinstance(n, UnaryOp):
            n.operand, body_index = self.flatten(n.operand, parent, body_index, True)
            
            return self.flattenNode(n, parent, body_index, shouldFlatten)
        elif isinstance(n, Call):
            if (isinstance(n.func, Name) and n.func.id == 'eval'):
                shouldNextFlatten = False
            else:
                shouldNextFlatten = True
                n.func, body_index = self.flatten(n.func, parent, body_index, shouldNextFlatten)

            for index, node in enumerate(n.args):
                n.args[index], body_index = self.flatten(node, parent, body_index, shouldNextFlatten)

            if not (isinstance(n.func, Name) and n.func.id in built_in_names):
                n.args = [Call(Name('get_free_vars', Load()), [n.func], [])] + n.args
                n.func = Call(Name('get_fun_ptr', Load()), [n.func], [])
            
                n.func, body_index = self.flattenNode(n.func, parent, body_index, True)
                n.args[0], body_index = self.flattenNode(n.args[0], parent, body_index, True)
            
            return self.flattenNode(n, parent, body_index, shouldFlatten)
        elif isinstance(n, Return):
            n.value, body_index = self.flatten(n.value, parent, body_index, True)

            return self.flattenNode(n, parent, body_index, shouldFlatten)
        elif isinstance(n, If):
            if (self.shouldInject):
                n.test = Call(Name("is_true", Load()), [n.test], [])

            if isinstance(n.test, Constant):
                n.test, body_index = self.flattenNode(n.test, parent, body_index, True)
            else:
                n.test, body_index = self.flatten(n.test, parent, body_index, True)

            sub_body_index = 0
            body_copy = n.body.copy()
            for index, node in enumerate(body_copy):
                sub_body_index = self.flatten(node, n.body, sub_body_index)[1]
                sub_body_index += 1

            sub_body_index = 0
            if n.orelse:
                orelse_copy = n.orelse.copy()
                for index, node in enumerate(orelse_copy):
                    sub_body_index = self.flatten(node, n.orelse, sub_body_index)[1]
                    sub_body_index += 1

            return (n, body_index)
        elif isinstance(n, IfExp):  
            new_var = self.var_title + str(self.var_count)
            self.var_count += 1
            new_node = If(n.test, [Assign([Name(new_var, Store())], n.body)], [Assign([Name(new_var, Store())], n.orelse)])
            new_node, body_index = self.flatten(new_node, parent, body_index)
            parent.insert(body_index, new_node)

            return (ast.copy_location(Name(new_var, Load()), n), body_index + 1)
        elif isinstance(n, While): 
            if (self.shouldInject):
                n.test = Call(Name("is_true", Load()), [n.test], [])

            prev_parent_len = len(parent)
            n.test, body_index = self.flatten(n.test, parent, body_index, True)
            dupe_num = len(parent) - prev_parent_len

            sub_body_index = 0
            body_copy = n.body.copy()
            for index, node in enumerate(body_copy):
                #print("before", sub_body_index)
                sub_body_index = self.flatten(node, n.body, sub_body_index)[1]
                #print("after", sub_body_index)
                
                sub_body_index += 1

            for num in range(dupe_num, 0, -1):
               n.body.append(parent[body_index - num])

            return (n, body_index)
        elif isinstance(n, FunctionDef):
            sub_body_index = 0
            for node in n.body.copy():
                sub_body_index = self.flatten(node, n.body, sub_body_index)[1]
                sub_body_index += 1

            self.root.body.remove(n)
            self.root.body.insert(0, n)

            return (n, body_index)
        else:
            for child_node in ast.iter_child_nodes(n):
                body_index = self.flatten(child_node, parent, body_index)[1]
            return (n, body_index)

    def get_free_and_bound_vars(self, n, free_var_set = set(), bound_var_set = set()) -> (set, set):
        if isinstance(n, FunctionDef) or isinstance(n, Lambda):
            #if (n.name not in built_in_names and n.name not in free_var_set and n.name not in bound_var_set):
                   # bound_var_set.add(n.name)

            for arg in n.args.args:
                if (arg.arg not in built_in_names and arg.arg not in free_var_set and arg.arg not in bound_var_set):
                    bound_var_set.add(arg.arg)

            for child_node in n.body.copy():
                self.get_free_and_bound_vars(child_node, free_var_set, bound_var_set)
        elif (isinstance(n, Name) and n.id not in built_in_names and n.id not in free_var_set and n.id not in bound_var_set):
            if (isinstance(n.ctx, Load)):
                free_var_set.add(n.id)
            else:
                bound_var_set.add(n.id)
        else:
            for child_node in ast.iter_child_nodes(n):
                self.get_free_and_bound_vars(child_node, free_var_set, bound_var_set)

        return free_var_set, bound_var_set

    def closure_convert(self, n, var_assignments = {}, parent = [], body_index = 0, prev = None):
        if isinstance(n, Module):
            for child in n.body.copy():
                new_node, body_index = self.closure_convert(child, var_assignments.copy(), n.body, body_index, n)  
                body_index += 1
        #elif isinstance(n, Assign):
            #new_node, body_index = self.closure_convert(n.targets[0], var_assignments, parent, body_index)

            #new_node, body_index = self.closure_convert(n.value, var_assignments, parent, body_index)
        elif isinstance(n, Subscript):
            new_node, body_index = self.closure_convert(n.value, var_assignments, parent, body_index, prev)
            new_node, body_index = self.closure_convert(n.slice, var_assignments, parent, body_index, prev)
            
            if isinstance(n.value, Name) and n.value.id in var_assignments:
                free_ver = n.value.id + "f"
                n.value = Subscript(Name(f"free_vars", n.ctx), Constant(var_assignments[n.value.id]), Load())
        elif isinstance(n, FunctionDef):
            var_count = 0
            free_vars, bound_vars = self.get_free_and_bound_vars(n, set(), set())

            #print("closure_convert", free_vars, bound_vars)

            new_var_assignments = var_assignments.copy()

            for free_var in free_vars:
                if free_var not in new_var_assignments:
                    new_var_assignments[free_var] = var_count
                    new_var_assignments[free_var + "f"] = self.free_var_count
                    var_count += 1

            n.args.args.insert(0, arg(f"free_vars"))
            self.free_var_count += 1

            insert_shift = 0
            for node in prev.body:
                if isinstance(node, Assign) and isinstance(node.value, List) and isinstance(node.value.elts[0], Constant) and node.value.elts[0].value == 0:
                    insert_shift += 1
                else:
                    break

            sub_body_index = 0
            for child in n.body.copy():
                new_node, sub_body_index = self.closure_convert(child, new_var_assignments, n.body, sub_body_index, n)
                sub_body_index += 1

            free_var_list = []
            for free_var in free_vars:
                if free_var in var_assignments:
                    free_var_list.append(Subscript(Name(f"free_vars", Load()), Constant(var_assignments[free_var]), Load()))
                else:
                    free_var_list.append(Name(free_var, Load()))
            
            

            if (n.name in self.free_vars):
                if n.name in var_assignments:
                    parent.insert(body_index + insert_shift, Assign([Subscript(Subscript(Name(f"free_vars", Store()), Constant(var_assignments[n.name]), Load()), Constant(0), Store())], Call(Name('inject_big', Load()), [Call(Name('create_closure', Load()), [Name(self.var_title + str(self.var_count), Load()), List(free_var_list)], [])], [])))
                else:
                    parent.insert(body_index + insert_shift, Assign([Subscript(Name(n.name, Load()), Constant(0), Store())], Call(Name('inject_big', Load()), [Call(Name('create_closure', Load()), [Name(self.var_title + str(self.var_count), Load()), List(free_var_list)], [])], [])))
            else:
                if n.name in var_assignments:
                     parent.insert(body_index + insert_shift, Assign([Subscript(Name(f"free_vars", Store()), Constant(var_assignments[n.name]), Load())], Call(Name('inject_big', Load()), [Call(Name('create_closure', Load()), [Name(self.var_title + str(self.var_count), Load()), List(free_var_list)], [])], [])))
                else:
                    parent.insert(body_index + insert_shift, Assign([Name(n.name, Load())], Call(Name('inject_big', Load()), [Call(Name('create_closure', Load()), [Name(self.var_title + str(self.var_count), Load()),  List(free_var_list)], [])], [])))
            n.name = self.var_title + str(self.var_count)
            parent.remove(n)
            self.root.body.insert(0, n)

            self.var_count += 1

            return n, body_index + 1
        elif isinstance(n, While):
            sub_body_index = 0
            for child in n.body.copy():
                new_node, sub_body_index = self.closure_convert(child, var_assignments, n.body, sub_body_index, prev)
                sub_body_index += 1
        elif isinstance(n, If):
            sub_body_index = 0
            for child in n.body.copy():
                new_node, sub_body_index = self.closure_convert(child, var_assignments, n.body, sub_body_index, prev)
                sub_body_index += 1

            sub_body_index = 0
            for child in n.orelse.copy():
                new_node, sub_body_index = self.closure_convert(child, var_assignments, n.orelse, sub_body_index, prev)
                sub_body_index += 1
        elif isinstance(n, IfExp):
            new_node, body_index = self.closure_convert(n.body, var_assignments, parent, body_index, prev)
            new_node, body_index = self.closure_convert(n.orelse, var_assignments, parent, body_index, prev)
        else:
            for child_node in ast.iter_child_nodes(n):
                new_node, body_index = self.closure_convert(child_node, var_assignments, parent, body_index, prev)

        return n, body_index
    
    def uniqify(self, n, var_assignments = {}):
        if (isinstance(n, Name) and n.id not in built_in_names):
            if (not (n.id in var_assignments)):
                var_assignments[n.id] = self.var_title + str(self.var_count)
                self.var_count += 1
            n.id = var_assignments[n.id]
        elif isinstance(n, Attribute):
            
            def traverse_attr(n):
                if isinstance(n, Attribute):
                    result = traverse_attr(n.value)

                    return result + "." + n.attr
                elif isinstance(n, Name):
                    return n.id

                return ""

            n.value = Name(traverse_attr(n.value), Load())
                
            if (isinstance(n.value, Name) and self.in_dict_ns(self.dep_map, n.value.id) and n.attr in self.access_dict_ns(self.dep_map, n.value.id)[1]):
                return var_assignments, Name(self.access_dict_ns(self.dep_map, n.value.id)[1][n.attr], n.ctx)
            else:
                #print(n.attr, n.value.id)
                sys.exit("Namespace or attribute does not exist.")
        elif isinstance(n, Return) or isinstance(n, Expr):
            n.value = self.uniqify(n.value, var_assignments)[1]
        elif isinstance(n, Subscript):
            n.value = self.uniqify(n.value, var_assignments)[1]
            n.slice = self.uniqify(n.slice, var_assignments)[1]
        elif isinstance(n, BinOp): 
            n.left = self.uniqify(n.left, var_assignments)[1]
            n.right = self.uniqify(n.right, var_assignments)[1]
        elif isinstance(n, BoolOp):
            n.values[0] = self.uniqify(n.values[0], var_assignments)[1]
            n.values[1] = self.uniqify(n.values[1], var_assignments)[1]
        elif isinstance(n, UnaryOp):
            n.operand = self.uniqify(n.operand, var_assignments)[1]
        elif isinstance(n, Call):
            n.func = self.uniqify(n.func, var_assignments)[1]

            for i, arg in enumerate(n.args):
                n.args[i] = self.uniqify(arg, var_assignments)[1]
        elif isinstance(n, Expr):
            n.operand = self.uniqify(n.operand, var_assignments)[1]
        elif isinstance(n, While):
            n.test = self.uniqify(n.test, var_assignments)[1]

            for i, child in enumerate(n.body):
                n.body[i] = self.uniqify(child, var_assignments)[1]
        elif isinstance(n, If):
            n.test = self.uniqify(n.test, var_assignments)[1]

            for i, child in enumerate(n.body):
                n.body[i] = self.uniqify(child, var_assignments)[1]

            for i, child in enumerate(n.orelse):
                n.orelse[i] = self.uniqify(child, var_assignments)[1]
        elif isinstance(n, IfExp):
            n.test = self.uniqify(n.test, var_assignments)[1]
            n.body = self.uniqify(n.body, var_assignments)[1]
            n.orelse = self.uniqify(n.orelse, var_assignments)[1]
        elif isinstance(n, List):
            for i, elt in enumerate(n.elts):
                n.elts[i] = self.uniqify(elt, var_assignments)[1]
        elif isinstance(n, Dict):
            for i, key in enumerate(n.keys):
                n.keys[i] = self.uniqify(key, var_assignments)[1]
            for i, value in enumerate(n.values):
                n.values[i] = self.uniqify(value, var_assignments)[1]
        elif isinstance(n, Assign):
            n.targets[0] = self.uniqify(n.targets[0], var_assignments)[1]
            n.value = self.uniqify(n.value, var_assignments)[1]
        elif isinstance(n, FunctionDef):
            if (not (n.name in var_assignments)):
                var_assignments[n.name] = self.var_title + str(self.var_count)
                self.var_count += 1
            n.name = var_assignments[n.name]

            sub_var_assignments = {}
            free_vars, bound_vars = self.get_free_and_bound_vars(n, set(), set())
            #print("free and bound vars:", n.name, free_vars, bound_vars)

            for free_var in free_vars:
                if (not (free_var in var_assignments)):
                    var_assignments[free_var] = self.var_title + str(self.var_count)
                    self.var_count += 1

            for key in var_assignments.keys():
                if key not in bound_vars:
                    sub_var_assignments[key] = var_assignments[key]

            #print("pre func var_assignments:", sub_var_assignments)

            

            for arg in n.args.args:
                if (not (arg.arg in sub_var_assignments)):
                    sub_var_assignments[arg.arg] = self.var_title + str(self.var_count)
                    self.var_count += 1
                arg.arg = sub_var_assignments[arg.arg]
                        
            for child_node in n.body.copy():
                self.uniqify(child_node, sub_var_assignments)
        else:
            for child_node in ast.iter_child_nodes(n):
                self.uniqify(child_node, var_assignments)

        return var_assignments, n

    def reassignVars(self, n):
        if (isinstance(n, Name) and n.id not in built_in_names):
            if (not (n.id in self.pre_assignments)):
                self.pre_assignments[n.id] = self.var_title + str(self.var_count)
                self.var_count += 1
            n.id = self.pre_assignments[n.id]
        
        if isinstance(n, Call):
            for arg in n.args:
                self.reassignVars(arg)
        else:
            for child_node in ast.iter_child_nodes(n):
                self.reassignVars(child_node)

    def flattenNode(self, n, parent, body_index, shouldFlatten):
        if (shouldFlatten):
            #print(self.var_title + str(self.var_count), body_index, parent)
            parent.insert(body_index, Assign([Name(self.var_title + str(self.var_count), Store())], n))
            self.var_count += 1
            return (ast.copy_location(Name(self.var_title + str(self.var_count - 1), ast.Load()), n), body_index + 1)
        return (n, body_index)

    def getVariables(self):
        return [self.var_title + str(i) for i in range(0, self.var_count)] + ['free_vars']

    def getFreeVars(self):
        return self.free_vars

    def explicate_pass(self, n, parent = [], body_index = 0):
        if isinstance(n, Module):
            for node in n.body.copy():
                body_index = self.explicate_pass(node, n.body, body_index)[1]
                body_index += 1

            n = ast.fix_missing_locations(n)

            return (n, body_index)
        elif isinstance(n, Assign):
            if isinstance(n.value, List):
                inject_arg = Call(Name('inject_int', Load()), [Constant(len(n.value.elts))], [])
                inject_arg, body_index = self.flatten(inject_arg.args[0], parent, body_index, True)
                create_arg = Call(Name('create_list', Load()), [inject_arg], [])
                create_arg, body_index = self.flatten(create_arg, parent, body_index, True)
                create_list = Call(Name('inject_big', Load()), [create_arg], [])

                for i, val in enumerate(n.value.elts):
                    body_index += 1
                    first_arg = Call(Name('inject_int', Load()), [Constant(i)], [])
                    second_arg = val
                    first_arg, body_index = self.flatten(first_arg.args[0], parent, body_index, True)
                    parent.insert(body_index, Expr(Call(Name('set_subscript', Load()), [n.targets[0], first_arg, second_arg], [])))           
                    
                n.value = create_list
            elif isinstance(n.value, Dict):
                create_arg = Call(Name('create_dict', Load()), [], [])
                create_arg, body_index = self.flatten(create_arg, parent, body_index, True)
                create_list = Call(Name('inject_big', Load()), [create_arg], [])

                for key, val in zip(n.value.keys, n.value.values):
                    body_index += 1
                    first_arg = key
                    second_arg = val
                    parent.insert(body_index, Expr(Call(Name('set_subscript', Load()), [n.targets[0], first_arg, second_arg], [])))           
                    
                n.value = create_list 
            elif isinstance(n.value, Subscript):
                n.value = Call(Name('get_subscript', Load()), [n.value.value, n.value.slice], [])

                return (n, body_index)
            else:
                n.value, body_index = self.explicate_pass(n.value, parent, body_index)
            
                self.explicate_pass(n.value, parent, body_index)

                if not isinstance(n.targets[0], Subscript):
                    
                    new_tree = self.explicate(n)

                    if (isinstance(new_tree, Module)):
                        del parent[body_index]

                        for node in new_tree.body:
                            parent.insert(body_index, node)
                            body_index += 1

                        body_index -= 1

            if isinstance(n.targets[0], Subscript):
                parent[body_index] = Expr(Call(Name('set_subscript', Load()), [n.targets[0].value, n.targets[0].slice, n.value], []))

                return (n, body_index)


            return (n, body_index)
        elif isinstance(n, Constant):
            if isinstance(n.value, bool):
                return self.flattenNode(Call(Name('inject_bool', Load()), [Constant(int(n.value))], []), parent, body_index, False)
            else:
                return self.flattenNode(Call(Name('inject_int', Load()), [n], []), parent, body_index, False)
        elif isinstance(n, FunctionDef):
            sub_body_index = 0
            body_copy = n.body.copy()
            for index, node in enumerate(body_copy):
                sub_body_index = self.explicate_pass(node, n.body, sub_body_index)[1]
                sub_body_index += 1

            return (n, body_index)
        elif isinstance(n, While): 
            '''
            n.test, body_index = self.flattenNode(n.test, parent, body_index, True)

            body_index -= 1
            
            new_tree = self.explicate(parent[body_index])

            if (isinstance(new_tree, Module)):
                del parent[body_index]

                for node in new_tree.body:
                        parent.insert(body_index, node)
                        body_index += 1
                       ''' 

            sub_body_index = 0
            body_copy = n.body.copy()
            for index, node in enumerate(body_copy):
                sub_body_index = self.explicate_pass(node, n.body, sub_body_index)[1]
                
                sub_body_index += 1

            return (n, body_index)
        elif isinstance(n, If):
            sub_body_index = 0
            body_copy = n.body.copy()
            for index, node in enumerate(body_copy):
                sub_body_index = self.explicate_pass(node, n.body, sub_body_index)[1]
                sub_body_index += 1

            sub_body_index = 0
            if n.orelse:
                orelse_copy = n.orelse.copy()
                for index, node in enumerate(orelse_copy):
                    sub_body_index = self.explicate_pass(node, n.orelse, sub_body_index)[1]
                    sub_body_index += 1

            return (n, body_index)
        else:
            for child_node in ast.iter_child_nodes(n):
                body_index = self.explicate_pass(child_node, parent, body_index)[1]
            return (n, body_index)
    
    def explicate(self, assign_node):
        if (isinstance(assign_node.targets[0], Attribute)):
            result_var_name = assign_node.targets[0].id
        else:
            result_var_name = assign_node.targets[0].id
        node = assign_node.value

        explicate_file = ''
        explicate_flat = ''
        explicate_ast = ''

        def get_var_name(node):
            if (isinstance(node, Name)):
                return node.id
            elif (isinstance(node, Constant)):
                return node.value
            return ''

        if (isinstance(node, BinOp)):
            sub_var_1 = node.left
            sub_var_2 = node.right

            if (isinstance(node.op, Add)):
                explicate_file = open(f"explicate_ops/explicate_add.py", "r")
                explicate_flat = open(f"explicate_ops/explicate_add_flat.py", "w")
                explicate_ast = open(f"explicate_ops/explicate_add_ast.py", "w")
        elif (isinstance(node, Compare)):
            sub_var_1 = node.left
            sub_var_2 = node.comparators[0]

            if (isinstance(node.ops[0], Eq)):
                explicate_file = open(f"explicate_ops/explicate_equals.py", "r")
                explicate_flat = open(f"explicate_ops/explicate_equals_flat.py", "w")
                explicate_ast = open(f"explicate_ops/explicate_equals_ast.py", "w")
            elif (isinstance(node.ops[0], NotEq)):
                explicate_file = open(f"explicate_ops/explicate_not_equals.py", "r")
                explicate_flat = open(f"explicate_ops/explicate_not_equals_flat.py", "w")
                explicate_ast = open(f"explicate_ops/explicate_not_equals_ast.py", "w")
            elif (isinstance(node.ops[0], Is)):
                explicate_file = open(f"explicate_ops/explicate_is.py", "r")
                explicate_flat = open(f"explicate_ops/explicate_is_flat.py", "w")
                explicate_ast = open(f"explicate_ops/explicate_is_ast.py", "w")
        elif (isinstance(node, BoolOp)):
            sub_var_1 = node.values[0]
            sub_var_2 = node.values[1]

            if (isinstance(node.op, And)):
                explicate_file = open(f"explicate_ops/explicate_and.py", "r")
                explicate_flat = open(f"explicate_ops/explicate_and_flat.py", "w")
                explicate_ast = open(f"explicate_ops/explicate_and_ast.py", "w")
            elif (isinstance(node.op, Or)):
                explicate_file = open(f"explicate_ops/explicate_or.py", "r")
                explicate_flat = open(f"explicate_ops/explicate_or_flat.py", "w")
                explicate_ast = open(f"explicate_ops/explicate_or_ast.py", "w")

        elif (isinstance(node, UnaryOp)):
            sub_var_1 = node.operand

            if (isinstance(node.op, USub)):
                explicate_file = open(f"explicate_ops/explicate_usub.py", "r")
                explicate_flat = open(f"explicate_ops/explicate_usub_flat.py", "w")
                explicate_ast = open(f"explicate_ops/explicate_usub_ast.py", "w")
            elif (isinstance(node.op, Not)):
                explicate_file = open(f"explicate_ops/explicate_not.py", "r")
                explicate_flat = open(f"explicate_ops/explicate_not_flat.py", "w")
                explicate_ast = open(f"explicate_ops/explicate_not_ast.py", "w")

        elif (isinstance(node, Call)):
            sub_var_1 = node.args[0]

            if (isinstance(node.func, Name) and node.func.id == "int"):
                explicate_file = open(f"explicate_ops/explicate_int.py", "r")
                explicate_flat = open(f"explicate_ops/explicate_int_flat.py", "w")
                explicate_ast = open(f"explicate_ops/explicate_int_ast.py", "w")

        '''
                elif (isinstance(node, Name)):
            sub_var_1 = node

            explicate_file = open(f"explicate_ops/explicate_test.py", "r")
            explicate_flat = open(f"explicate_ops/explicate_test_flat.py", "w")
            explicate_ast = open(f"explicate_ops/explicate_test_ast.py", "w")
        '''
        

        if (explicate_file == '' or explicate_flat == '' or explicate_ast == ''):
            return assign_node
            
        prog = explicate_file.read()
        file_tree = ast.parse(prog)
        self.shouldInject = False
        self.uniqify(file_tree, {})
        self.flatten(file_tree)
        self.shouldInject = True

        #print(ast.dump(file_tree, indent=4))

        sub_name = ''

        tmp1 = file_tree.body[0]
        if (isinstance(tmp1, Assign) and isinstance(tmp1.value, Name)):
            #print(tmp1.value.id)
            sub_name = self.var_title + str(int(tmp1.value.id[1:]) + 1)
            #print(sub_name)
            tmp1.value = sub_var_1

        tmp2 = file_tree.body[1]
        if (isinstance(tmp2, Assign) and isinstance(tmp2.value, Name)):
            #print(tmp2.value.id)
            sub_name = self.var_title + str(int(tmp2.value.id[1:]) + 1)
            #print(sub_name)
            tmp2.value = sub_var_2

        self.sub_explicate_tree(file_tree, sub_name, result_var_name)

        explicate_ast.write(ast.dump(file_tree, indent=4))
        explicate_flat.write(ast.unparse(file_tree))

        return file_tree

    def sub_explicate_tree(self, explicate_ast, sub_name, new_var):
        if (isinstance(explicate_ast, Assign) and isinstance(explicate_ast.targets[0], Name) and explicate_ast.targets[0].id == sub_name):
            explicate_ast.targets[0].id = new_var
        else:
            for child_node in ast.iter_child_nodes(explicate_ast):
                self.sub_explicate_tree(child_node, sub_name, new_var)

    def unify_defs(self, n, lambda_num, parent = [], body_index = 0):
        """
        converts the body of Lambda to Return(body)
        converts Lambdas to functions
        """
        if isinstance(n, Module):
            for node in n.body.copy():
                new_node, body_index = self.unify_defs(node, lambda_num, n.body, body_index)
                body_index += 1
        elif isinstance(n, Assign) or isinstance(n, Return):
            n.value, body_index = self.unify_defs(n.value, lambda_num, parent, body_index)
        elif isinstance(n, Call):
            n.func, body_index = self.unify_defs(n.func, lambda_num, parent, body_index)

            for arg in n.args:
                arg, body_index = self.unify_defs(arg, lambda_num, parent, body_index)
        elif isinstance(n, List):
            for i, elt in enumerate(n.elts):
                n.elts[i], body_index = self.unify_defs(elt, lambda_num, parent, body_index)
        elif isinstance(n, Lambda):
            new_func = FunctionDef('Lambda' + str(lambda_num[0]), args=n.args, body=[Return(n.body)], decorator_list=[])
            parent.insert(body_index, new_func)
            new_node = Name('Lambda' + str(lambda_num[0]), Load())
            #print(ast.dump(n, indent=4))
            lambda_num[0] += 1

            self.unify_defs(new_func, lambda_num, parent, body_index)

            return new_node, body_index + 1
        elif isinstance(n, While) or isinstance(n, FunctionDef):
            sub_body_index = 0
            #print(ast.dump(self.root, indent=4))
            for child in n.body.copy():
                new_node, sub_body_index = self.unify_defs(child, lambda_num, n.body, sub_body_index)
                sub_body_index += 1
        elif isinstance(n, If):
            sub_body_index = 0
            for child in n.body.copy():
                new_node, sub_body_index = self.unify_defs(child, lambda_num, n.body, sub_body_index)
                sub_body_index += 1

            sub_body_index = 0
            for child in n.orelse.copy():
                new_node, sub_body_index = self.unify_defs(child, lambda_num, n.body, sub_body_index)
                sub_body_index += 1
        elif isinstance(n, IfExp):
            new_node, body_index = self.unify_defs(n.body, lambda_num, parent, body_index)
            new_node, body_index = self.unify_defs(n.orelse, lambda_num, parent, body_index)
        else:
            for child in ast.iter_child_nodes(n):
                self.unify_defs(child, lambda_num, parent, body_index)

        return n, body_index
    
    def get_free_vars(self, lst: set(), n: AST, parent = None):
        if isinstance(n, Module):
            for node in ast.iter_child_nodes(n):
                self.get_free_vars(lst, node, n)
        elif isinstance(n, FunctionDef):
            local_free_vars = self.get_free_and_bound_vars(n, set(), set())[0]
            
            for free_var in local_free_vars:
                if free_var not in self.crossed_off_vars and free_var not in self.dep_free_vars:
                    self.crossed_off_vars.add(free_var)

                    if (free_var in self.dep_vars):
                        parent.body.insert(0, Assign([Name(free_var, Store())], List([Name(free_var, Load())])))
                    else:
                        parent.body.insert(0, Assign([Name(free_var, Store())], List([Constant(0)])))

            lst.update(local_free_vars)
            for node in n.body.copy():
                self.get_free_vars(lst, node, n)
        else:
            for node in ast.iter_child_nodes(n):
                self.get_free_vars(lst, node, parent)
    
    def heapify(self, n: AST, free_vars: set(), indexed: set(), prev = None):
        if isinstance(n, Module):
            indexed.update(self.dep_free_vars)

            for node in ast.iter_child_nodes(n):
                self.heapify(node, free_vars, indexed, prev)
        elif isinstance(n, Name) and (n.id in free_vars or n.id in indexed):
            return Subscript(n, Constant(0), Load())
        elif isinstance(n, Return) or isinstance(n, Expr):
            n.value = self.heapify(n.value, free_vars, indexed, prev)
        elif isinstance(n, Subscript):
            n.value = self.heapify(n.value, free_vars, indexed, prev)
            n.slice = self.heapify(n.slice, free_vars, indexed, prev)
        elif isinstance(n, BinOp): 
            n.left = self.heapify(n.left, free_vars, indexed, prev)
            n.right = self.heapify(n.right, free_vars, indexed, prev)
        elif isinstance(n, BoolOp):
            n.values[0] = self.heapify(n.values[0], free_vars, indexed, prev)
            n.values[1] = self.heapify(n.values[1], free_vars, indexed, prev)
        elif isinstance(n, UnaryOp):
            n.operand = self.heapify(n.operand, free_vars, indexed, prev)
        elif isinstance(n, Call):
            n.func = self.heapify(n.func, free_vars, indexed, prev)

            for i, arg in enumerate(n.args):
                n.args[i] = self.heapify(arg, free_vars, indexed, prev)
        elif isinstance(n, Expr):
            n.operand = self.heapify(n.operand, free_vars, indexed, prev)
        elif isinstance(n, While):
            n.test = self.heapify(n.test, free_vars, indexed, prev)

            for i, child in enumerate(n.body):
                n.body[i] = self.heapify(child, free_vars, indexed, prev)
        elif isinstance(n, If):
            n.test = self.heapify(n.test, free_vars, indexed, prev)

            for i, child in enumerate(n.body):
                n.body[i] = self.heapify(child, free_vars, indexed, prev)

            for i, child in enumerate(n.orelse):
                n.orelse[i] = self.heapify(child, free_vars, indexed, prev)
        elif isinstance(n, IfExp):
            n.test = self.heapify(n.test, free_vars, indexed, prev)
            n.body = self.heapify(n.body, free_vars, indexed, prev)
            n.orelse = self.heapify(n.orelse, free_vars, indexed, prev)
        elif isinstance(n, List):
            for i, elt in enumerate(n.elts):
                n.elts[i] = self.heapify(elt, free_vars, indexed, prev)
        elif isinstance(n, Dict):
            for i, key in enumerate(n.keys):
                n.keys[i] = self.heapify(key, free_vars, indexed, prev)
            for i, value in enumerate(n.values):
                n.values[i] = self.heapify(value, free_vars, indexed, prev)
        elif isinstance(n, Assign):
            flag = True
            #print("indexed:", indexed)
            #print("free_vars:", free_vars)
            if isinstance(n.targets[0], Name) and n.targets[0].id in free_vars:
                if n.targets[0].id not in indexed:
                    if isinstance(prev, FunctionDef):
                        for arg in prev.args.args:
                            if n.targets[0].id == arg.arg and isinstance(n.value, List):
                                flag = False
                                n.value.elts[0] = Name(arg.arg, Load())
                    elif n.targets[0].id in self.dep_vars:
                        flag = False
                    indexed.add(n.targets[0].id)
                else:
                    n.targets[0] = Subscript(n.targets[0], Constant(0), Load())
            
            if (flag):
                n.value = self.heapify(n.value, free_vars, indexed, prev)
            
           
        elif isinstance(n, FunctionDef):
            for child in n.body:
                self.heapify(child, free_vars, indexed, n)
        else:
            for node in ast.iter_child_nodes(n):
                self.heapify(node, free_vars, indexed, prev)

        return n

    

