'''
баланс скобок
'''

from aisd01_04 import Stack


def is_balanced(inputs):

    if inputs[0] == ')' or len(inputs) % 2 != 0:
        return False

    stack = Stack()
    stack.push(inputs[0])

    for bracket in inputs[1:]:
        if bracket == ')':
            stack.pop()
        else:
            stack.push(bracket)

    return not stack.size()


if __name__ == '__main__':
    for test in [
        "(()((())()))",
        '(()()(()',
        "())(", "))((", "((())",
        "()(()())()((()())())"
    ]:
        print(is_balanced(test))
