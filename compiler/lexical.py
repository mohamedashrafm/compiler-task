import tokenize
from io import BytesIO

def lexical_analysis(source_code):
    # Convert the source code into a bytes-like object
    source_bytes = source_code.encode('utf-8')

    # Create a BytesIO object to simulate a file-like object
    source_file = BytesIO(source_bytes)

    # Tokenize the source code
    tokens = tokenize.tokenize(source_file.readline)

    # Display the tokens
    for tok in tokens:
        print(tok)

# Example usage
source_code = """
def add_numbers(a, b):
    return a + b

result = add_numbers(10, 20)
print(result)
"""

lexical_analysis(source_code)