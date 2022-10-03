def is_right(expression):
    open_brackets = ('(', '[', '{')
    close_brackets = (')', ']', '}')
    stack = []
    for i in expression:
        if i in open_brackets:
            stack.append(i)
        if i in close_brackets:
            if len(stack) == 0:
                return True
            index = close_brackets.index(i)
            bracket_open = open_brackets[index]
            if stack[-1] == bracket_open:
                stack = stack[:-1]
            else:
                return False
    return (not stack)
