import pytest
from aisd02_07_Heap import *


@pytest.fixture
def heap():
    return Heap()


def test_make_heap(heap):
    heap.MakeHeap([4, 5, 2], 0)
    assert heap.HeapArray == [4]
    heap.MakeHeap([4, 5, 2], 1)
    assert heap.HeapArray == [5, 4, 2]
    heap.MakeHeap([4, 5, 2, 3], 2)
    assert heap.HeapArray == [5, 4, 2, 3, None, None, None]


def test_get_max(heap):
    assert heap.GetMax() == -1
    heap.HeapArray = [None]
    assert heap.GetMax() == -1
    heap.HeapArray = [2]
    assert heap.GetMax() == 2
    assert len(heap.HeapArray) == 0
    heap.HeapArray = [3, None]
    assert heap.GetMax() == 3
    assert len(heap.HeapArray) == 1
    assert heap.HeapArray[0] is None
    heap.HeapArray = [5, 4, 3]
    assert heap.GetMax() == 5

    heap.MakeHeap([11, 9, 4, 7, 8, 3, 1, 2, 5, 6], 3)
    assert heap.GetMax() == 11
    assert heap.GetMax() == 9


def test_add(heap):
    assert not heap.Add(3)
    heap.HeapArray = [None, None, None]
    assert heap.Add(4)
    assert heap.Add(5)
    assert heap.Add(2)
    assert not heap.Add(12)
