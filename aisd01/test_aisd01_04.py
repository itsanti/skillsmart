import pytest
from aisd01_04 import Stack


@pytest.fixture
def stack():
    stack = Stack()
    return stack


def test_size(stack):
    assert stack.size() == 0


def test_pop(stack):
    assert stack.pop() is None
    stack.push(12)
    stack.push(13)
    assert stack.pop() == 13
    assert stack.size() == 1


def test_push(stack):
    stack.push(13)
    assert stack.size() == 1


def test_peek(stack):
    assert stack.peek() is None
    stack.push(12)
    stack.push(13)
    assert stack.peek() == 13
