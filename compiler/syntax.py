import ast


def syntax_analysis(source_code):
    try:
        # Parse the source code into an Abstract Syntax Tree (AST)
        parsed_ast = ast.parse(source_code)

        # Print the AST
        print_ast(parsed_ast)

        # You can perform further analysis on the AST if needed

    except SyntaxError as e:
        print(f"Syntax error: {e}")


def print_ast(node, indent=0):
    # Helper function to print the AST
    print("  " * indent + f"{node._class.name_}")
    for child_node in ast.iter_child_nodes(node):
        print_ast(child_node, indent + 1)


# Example usage
source_code = """
def add_numbers(a, b):
    return a + b

result = add_numbers(10, 20)
print(result)
"""

syntax_analysis(source_code)