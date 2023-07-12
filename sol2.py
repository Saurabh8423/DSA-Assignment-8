def checkValidString(s):
    stack = []

    for c in s:
        if c == '(' or c == '*':
            stack.append(c)
        elif c == ')':
            if len(stack) == 0:
                return False
            if stack[-1] == '(':
                stack.pop()
            else:
                # Find a matching opening parenthesis or treat '*' as empty string
                i = len(stack) - 1
                while i >= 0 and stack[i] != '(':
                    i -= 1
                if i >= 0:
                    stack.pop(i)
                else:
                    stack.pop()

    # Match remaining opening parentheses with asterisks or closing parentheses
    while len(stack) > 0:
        if stack[-1] == '(':
            i = len(stack) - 1
            while i >= 0 and stack[i] != '*':
                i -= 1
            if i >= 0:
                stack.pop(i)
                stack.pop()
            else:
                return False
        else:
            stack.pop()

    return True
s = "()"
print(checkValidString(s))  # Output: True

