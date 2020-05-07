def is_balanced_parenthesis(parens_string):
    stack = []
    for char in parens_string:
        if char == "(":
            stack.append(True)
        elif char == ")" and len(stack) > 0:
            stack.pop()

    return len(stack) == 0

