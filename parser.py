import lark
from lark import Lark, ast_utils, Transformer, v_args, indenter
import ast
from ast import * 


class ToAst(Transformer):
    """Define extra transformation functions, 
    for rules that don't correspond to an AST class."""

    def parens(self, x):
        return x[1]

    def constant(self, x):
        return Constant(int(x[0].value))

    def const_true(self, x):
        return Constant(True)
    
    def const_false(self, x):
        return Constant(False)
      
    def binop(self, x):
        return BinOp(x[0], Add(), x[2])

    def unaryop(self, x):
        return UnaryOp(USub(), x[1])

    def expr(self, x):
        if isinstance(x[0], lark.Token) and x[0].type == "CNAME":
            return Name(x[0].value, Load())
        elif len(x) == 1:
            return x[0]
        return x
    
    def assign(self, x):
        if isinstance(x[0], Subscript):
            return Assign([x[0]], x[2])
        return Assign([Name(x[0].value, Store())], x[2])
    
    def statement(self, x): # comment / NL
        return
   
    def call(self, x):
        output = Call(Name(x[0].value, Load()), x[2:-1], [])
        # if (x[0].value == 'print'):
        #     return Expr(output)
        return output

    def and_stmt(self, x):
        return BoolOp(And(), [x[0], x[1]]) 

    def or_stmt(self, x):
        return BoolOp(Or(), [x[0], x[1]]) 

    def not_stmt(self, x):
        return UnaryOp(Not(), x[0]) 
    # def not_stmt(self, x):
    #     x = [node for node in x if node is not None]
    #     if isinstance(x[0], lark.Token) and x[0].value == "int":
    #         return Call(Name("int", Load()), [UnaryOp(Not(), x[3])] )
    #     return UnaryOp(Not(), x[1]) 
    
    def conditional(self, x):
        return IfExp(x[1], x[0], x[2]) # IfExp(test, body, orelse)

    def eq(self, x):
        return Compare(x[0], [Eq()], [x[2]])  # Compare(left, ops, comparators)
    # def eq(self, x):
    #     x = [node for node in x if node is not None]
    #     print(x)
    #     if isinstance(x[0], lark.Token) and x[0].value == "int":
    #         return Call(Name("int", Load()), [Compare(x[2], [Eq()], [x[4]])] )
    #     return Compare(x[0], [Eq()], [x[2]])  # Compare(left, ops, comparators)

    def neq(self, x):
        return Compare(x[0], [NotEq()], [x[2]])  # Compare(left, ops, comparators)
    # def neq(self, x):
    #     x = [node for node in x if node is not None]
    #     if isinstance(x[0], lark.Token) and x[0].value == "int":
    #         return Call(Name("int", Load()), [Compare(x[2], [NotEq()], [x[4]])] )
    #     return Compare(x[0], [NotEq()], [x[2]])  # Compare(left, ops, comparators)

    def is_stmt(self, x):
        return Compare(x[0], [Is()], [x[1]])

    def if_stmt(self, x):
        if len(x) < 3: # no else
            return If(x[0], x[1], [])
        return If(x[0], x[1], x[2])

    def while_stmt(self, x):
        return While(x[0], x[1], []) # While(test, body, orelse)

    def func_def(self, x):
        args = [arg(n.value) for n in x[1:-1]]
        return FunctionDef(x[0].value, arguments([], args, [], [], [], [], []), x[-1], []) 

    def lambda_def(self, x):
        args = [arg(n.value) for n in x[0:-1]]
        return Lambda(arguments([], args, [], [], [], [], []), x[-1])

    def def_suite(self, x):
        nodes = []
        for child in x:
            if child:
                nodes.append(child)
        return nodes

    def return_stmt(self, x):
        return Return(x[0])
    
    def test(self, x):
        return x[0]
    def test_parens(self, x):
        return x[1]

    def lst(self, x):
        elts = []
        for child in x:
            elts.append(child)
        return List(elts, Load()) 

    def dct(self, x):
        keys = x[0::2]
        elts = x[1::2]
        return Dict(keys, elts) 

    def subscr(self, x):
        return Subscript(x[0], x[1], Load())

    def suite(self, x):
        nodes = []
        for child in x:
            if child:
                nodes.append(child)
        return nodes

    def start(self, x):
        nodes = []
        for child in x:
            if child: # check child is not None (comment/NL)
                if isinstance(child, Call): # trying this for now
                    child = Expr(child)
                nodes.append(child)
        return Module(nodes, [])


class PythonIndenter(indenter.Indenter):
    NL_type = '_NL'
    OPEN_PAREN_types = []
    CLOSE_PAREN_types = []
    INDENT_type = '_INDENT'
    DEDENT_type = '_DEDENT'
    tab_len = 8

class Parser():
    def parse(self, text):
        # parser = Lark.open('./python.lark', \
        #     rel_to=__file__, parser="earley", postlex=PythonIndenter())
        parser = Lark.open('./python1.lark', \
            rel_to=__file__, parser="earley", postlex=PythonIndenter())
        tree = parser.parse(text)
        print(tree.pretty())
        # print()
        tree = ToAst().transform(tree)
        ast.fix_missing_locations(tree)
        return tree
