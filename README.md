# Multithreaded Python to x86 Compiler

This is the repository for our python to x86 compiler, which implements multi-threading, along with the *import* keyword, which allows the inclusion of dependencies in files.

# Python Subset

- Int, boolean, list, and dictionary types
- Control flow for if-else statements and while loops
- Function definitions and calls, including lambdas
- Dynamic typing

# Implementation:

- Explication for dynamic typing
- Parsing using custom lark grammar
- Abstract Syntax Tree (AST) creation
- Multithreading for multiple files and compilation tasks that are independant of eachother
- Interference graph implementation
- Register allocation using graph coloring

# Usage

You may compile a set of files using the command, which will result in an x86 equivalent of the program:

```bash
$ python3 compiler.py <file1> <file2> <...>
```

# Tests

There have been a couple of new tests included, but should not change how tests are run. This includes automated tests.
