import ast
from lark import indenter, Lark
from Graph import *
# from ast import *
from parser import Parser
from compilertools import *


file = "./test.py"
with open(file) as f:
    prog = f.read()

file_tree = ast.parse(prog)
print(ast.dump(file_tree, indent=4))

file_tree = Parser().parse(prog) # parse
print(ast.dump(file_tree, indent=4))

unify_defs(file_tree)
print(ast.dump(file_tree, indent=4))


# Flattener(file_tree)
# print(ast.dump(file_tree, indent=4))

# flatpy = open(f"flat_add.py", "w")
# flatpy.write(ast.unparse(file_tree))

# flatast = open(f"flat_ast_add.txt", "w")
# flatast.write(ast.dump(file_tree, indent=4))