# s = "(())()"
s = "()))(("


def is_correct_parenthesis(string):
    stack = []

    for ch in string:
        if ch == '(':
            stack.append(ch)
        else:
            if not stack:
                return False
            stack.pop()

    return len(stack) == 0



print(is_correct_parenthesis(s))  # True 를 반환해야 합니다!