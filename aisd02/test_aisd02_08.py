import pytest
from aisd02_08_SimpleGraph import *


@pytest.fixture
def sg():
    size = 1
    return SimpleGraph(size)


@pytest.fixture
def sg5():
    sg5 = SimpleGraph(5)
    sg5.AddVertex('A')
    sg5.AddVertex('B')
    sg5.AddVertex('C')
    sg5.AddVertex('D')
    sg5.AddVertex('E')
    return sg5


def test_add_vertex(sg):
    assert sg.AddVertex('A') == 0
    assert sg.AddVertex('B') == -1


def test_remove_vertex(sg):
    assert False


def test_is_edge(sg, sg5):
    assert not sg.IsEdge(0, 0)


def test_add_edge(sg5):
    assert not sg5.IsEdge(0, 1)
    assert sg5.AddEdge(0, 1)
    assert sg5.IsEdge(0, 1)


def test_remove_edge(sg5):
    sg5.AddEdge(0, 1)
    assert sg5.IsEdge(0, 1)
    assert sg5.RemoveEdge(0, 1)
    assert not sg5.IsEdge(0, 1)


def test_remove_edge_full(sg5):
    sg5.AddEdge(0, 1)
    sg5.AddEdge(0, 2)
    sg5.AddEdge(0, 3)
    assert sum([sum(row) for row in sg5.m_adjacency]) == 6
    assert sg5.RemoveVertex(0)
    assert sum([sum(row) for row in sg5.m_adjacency]) == 0
