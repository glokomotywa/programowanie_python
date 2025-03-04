def is_balanced(expression: str):
    matching_brackets = {')': '(', ']': '[', '}': '{' }
    stack = []

    for char in expression:
        if char in '([{':
            stack.append(char)
        elif char in ')]}':
            if not stack or stack[-1] != matching_brackets[char]:
                return False
            stack.pop()

    if(len(stack) == 0):
        return True

    return False


valid_expression = '(1 + 2 - {3 + 5} + [1 - 2])'
bad_expression = '({[]}{()}[([)]])'

print(is_balanced(valid_expression))
print(is_balanced(bad_expression))
