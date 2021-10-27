import pytest
from aisd01_05 import Queue


@pytest.fixture
def queue():
    queue = Queue()
    return queue


def test_size(queue):
    assert queue.size() == 0
    queue.enqueue(3)
    assert queue.size() == 1


def test_enqueue(queue):
    queue.enqueue(3)
    queue.enqueue(4)
    assert queue.queue[-1] == 4


def test_dequeue(queue):
    queue.enqueue(3)
    queue.enqueue(4)
    assert queue.dequeue() == 3
    assert queue.dequeue() == 4
    assert queue.dequeue() is None
