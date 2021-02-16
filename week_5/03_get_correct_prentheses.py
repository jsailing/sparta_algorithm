from collections import deque

balanced_parentheses_string = "()))((()"


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


def separete_to_u_v(string):
    left, right = 0, 0
    u, v = '', ''
    queue = deque(string)

    while queue:
        ch = queue.popleft()
        u += ch

        if ch == '(':
            left += 1
        else:
            right += 1

        if left == right:
            break

    return u, v.join(queue)


def reverse_parentheses(string):
    reversed_string = ""

    for ch in string:
        if ch == '(':
            reversed_string += ")"
        else:
            reversed_string += "("

    return reversed_string


def change_to_correct_parentheses(string):
    if string == '':
        return ''

    u, v = separete_to_u_v(string)

    if is_correct_parenthesis(u):
        return u + change_to_correct_parentheses(v)
    else:
        return '(' + change_to_correct_parentheses(v) + ')' + reverse_parentheses(u[1:-1])


def get_correct_parentheses(balanced_parentheses_string):
    if is_correct_parenthesis(balanced_parentheses_string):
        return balanced_parentheses_string
    else:
        return change_to_correct_parentheses(balanced_parentheses_string)


print(get_correct_parentheses(balanced_parentheses_string))  # "()(())()"가 반환 되어야 합니다!