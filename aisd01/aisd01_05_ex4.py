'''
6.4. Попробуйте реализовать очередь с помощью двух стеков.
'''

from aisd01_04 import Stack


class StackQueue:
    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()

    def enqueue(self, item):
        if self.size() < 1:
            self.stack1.push(item)
        else:
            while self.size():
                self.stack2.push(self.stack1.pop())
            self.stack1.push(item)
            while self.stack2.size():
                self.stack1.push(self.stack2.pop())

    def dequeue(self):
        if self.size() > 0:
            return self.stack1.pop()
        return None

    def size(self):
        return self.stack1.size()


if __name__ == '__main__':
    sq = StackQueue()
    assert sq.size() == 0
    sq.enqueue(3)
    sq.enqueue(4)
    assert sq.dequeue() == 3
    assert sq.dequeue() == 4
    assert sq.dequeue() is None
