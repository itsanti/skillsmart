import pytest
from aisd02_12_SimpleGraph_WeakVertices import *


@pytest.fixture
def sg9():
    sg9 = SimpleGraph(9)
    for v in range(1, 10):
        sg9.AddVertex(v)

    sg9.AddEdge(0, 1)
    sg9.AddEdge(0, 2)
    sg9.AddEdge(0, 3)

    sg9.AddEdge(1, 0)
    sg9.AddEdge(1, 3)
    sg9.AddEdge(1, 4)

    sg9.AddEdge(2, 0)
    sg9.AddEdge(2, 3)

    sg9.AddEdge(3, 0)
    sg9.AddEdge(3, 1)
    sg9.AddEdge(3, 2)
    sg9.AddEdge(3, 5)

    sg9.AddEdge(4, 1)
    sg9.AddEdge(4, 5)

    sg9.AddEdge(5, 4)
    sg9.AddEdge(5, 3)
    sg9.AddEdge(5, 6)
    sg9.AddEdge(5, 7)

    sg9.AddEdge(6, 5)
    sg9.AddEdge(6, 7)

    sg9.AddEdge(7, 6)
    sg9.AddEdge(7, 5)
    sg9.AddEdge(7, 8)

    sg9.AddEdge(8, 7)

    return sg9


def test_WeakVertices(sg9):
    assert len(sg9.WeakVertices()) == 2

