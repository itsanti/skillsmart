'''
тест строки на полиндром с Deque
'''

from aisd01_06 import Deque


def is_polindrome(inputs):
    polindrome = True
    deque = Deque()
    for char in inputs:
        deque.addTail(char)

    while deque.size() > 1 and polindrome:
        if deque.removeFront() != deque.removeTail():
            polindrome = False
    return polindrome


if __name__ == '__main__':
    for test in [
        "abcddcba",
        'abc',
        "abcba",
        "a"
    ]:
        print(is_polindrome(test))
