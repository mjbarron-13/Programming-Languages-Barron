import re


def count_tokens(expression):
    # Extract tokens (numbers, operators, parentheses)
    tokens = re.findall(r"\d+|\S", expression)
    return len(tokens), tokens  # Returning total token count and token list


def calculator():
    print("Simple Python Calculator")
    print("Available operators: +, -, *, /, **")

    while True:
        expression = input("Enter an expression (e.g., 5 + 3): ")

        # Count tokens
        num_tokens, tokens = count_tokens(expression)

        try:
            # Evaluate the expression
            result = eval(expression)
            print(f"Result: {result}")
        except Exception as e:
            print(f"Error: {e}")

        print(f"Number of tokens: {num_tokens} b {tokens}")


if __name__ == "__main__":
    calculator()
