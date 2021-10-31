import pytest
from aisd01_06 import Deque


@pytest.fixture
def deque():
    deque = Deque()
    return deque


def test_add_front(deque):
    deque.addFront(1)
    deque.addFront(2)
    assert deque.deque[1] == 1


def test_add_tail(deque):
    deque.addTail(1)
    deque.addTail(2)
    assert deque.deque[-2] == 1


def test_remove_front(deque):
    deque.addFront(1)
    deque.addFront(2)
    assert deque.removeFront() == 2
    assert deque.removeFront() == 1
    assert deque.removeFront() is None


def test_remove_tail(deque):
    deque.addFront(1)
    deque.addFront(2)
    assert deque.removeTail() == 1
    assert deque.removeTail() == 2
    assert deque.removeTail() is None


def test_size(deque):
    assert deque.size() == 0
    deque.addFront(1)
    assert deque.size() == 1
