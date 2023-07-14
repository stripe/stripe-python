# This script crawls the AST of a .pyi file and sorts
# the contents of each node alphabetically (but hoisting
# imports to the top). This is used by check_stubs.sh to
# produce more interpretable diffs. Delete this after
# check_stubs.sh is no longer needed.

import ast
import sys


def sort_key(x):
    return ("import" not in ast.unparse(x)), ast.unparse(x)


def sort_ast_nodes(node):
    for _, value in ast.iter_fields(node):
        if isinstance(value, list):
            value.sort(key=sort_key)
            for item in value:
                if isinstance(item, ast.AST):
                    sort_ast_nodes(item)
        elif isinstance(value, ast.AST):
            sort_ast_nodes(value)


def sort_input(input_code):
    module_ast = ast.parse(input_code)
    module_ast.body.sort(key=sort_key)
    sort_ast_nodes(module_ast)
    return ast.unparse(module_ast)


if __name__ == "__main__":
    input_code = sys.stdin.read()
    sys.stdout.write(sort_input(input_code) + "\n")
