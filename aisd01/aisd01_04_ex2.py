'''
Постфиксная запись выражения
'''

from aisd01_04 import Stack


def calculate_postfix(inputs):
    s1 = Stack()
    s2 = Stack()
    result = None

    for o in reversed(inputs.split()):
        s1.push(o)

    while s1.size():
        el: str = s1.pop()
        if el.isdigit():
            s2.push(el)
        else:
            if el == '+':
                s2.push(int(s2.pop()) + int(s2.pop()))
            elif el == '*':
                s2.push(int(s2.pop()) * int(s2.pop()))
            elif el == '=':
                result = s2.pop()

    return result


if __name__ == '__main__':
    for test in [
        "1 2 + 3 * =",
        "8 2 + 5 * 9 + =",
        "2 3 *",
        "2 3 + 2 * ="
    ]:
        print(calculate_postfix(test))
