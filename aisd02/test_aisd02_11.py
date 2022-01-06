import pytest
from aisd02_11_SimpleGraph_BreadthFirstSearch import *


@pytest.fixture
def sg5():
    sg5 = SimpleGraph(5)
    sg5.AddVertex('A')
    sg5.AddVertex('B')
    sg5.AddVertex('C')
    sg5.AddVertex('D')
    sg5.AddVertex('E')

    sg5.AddEdge(0, 1)
    sg5.AddEdge(0, 2)
    #sg5.AddEdge(0, 3)

    sg5.AddEdge(1, 0)
    sg5.AddEdge(1, 3)
    #sg5.AddEdge(1, 4)

    sg5.AddEdge(2, 0)
    sg5.AddEdge(2, 3)

    #sg5.AddEdge(3, 0)
    sg5.AddEdge(3, 1)
    sg5.AddEdge(3, 2)
    sg5.AddEdge(3, 3)
    sg5.AddEdge(3, 4)

    #sg5.AddEdge(4, 1)
    sg5.AddEdge(4, 3)
    return sg5


@pytest.fixture
def sg3():
    sg3 = SimpleGraph(3)
    sg3.AddVertex('A')
    sg3.AddVertex('B')
    sg3.AddEdge(0, 1)
    sg3.AddVertex('C')
    return sg3


def test_BreadthFirstSearch(sg3, sg5):
    print(sg3.BreadthFirstSearch(0, 2))
    print(sg3.BreadthFirstSearch(0, 1))
    print(sg5.BreadthFirstSearch(0, 1))
    print(sg5.BreadthFirstSearch(4, 1))
    print(sg5.BreadthFirstSearch(0, 4))
