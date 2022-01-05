import pytest
from aisd02_09_Forest import *


@pytest.fixture
def st():
    st = SimpleTree(None)
    st.AddChild(None, SimpleTreeNode(1, None))
    st.AddChild(st.Root, SimpleTreeNode(2, None))
    st.AddChild(st.Root, SimpleTreeNode(3, None))
    st.AddChild(st.Root, SimpleTreeNode(6, None))

    st.AddChild(st.Root.Children[0], SimpleTreeNode(5, None))
    st.AddChild(st.Root.Children[0], SimpleTreeNode(7, None))

    st.AddChild(st.Root.Children[1], SimpleTreeNode(4, None))

    st.AddChild(st.Root.Children[2], SimpleTreeNode(8, None))

    st.AddChild(st.Root.Children[2].Children[0], SimpleTreeNode(9, None))
    st.AddChild(st.Root.Children[2].Children[0], SimpleTreeNode(10, None))

    st.AddChild(st.Root.Children[2].Children[0].Children[1], SimpleTreeNode(11, None))
    st.AddChild(st.Root.Children[2].Children[0].Children[1].Children[0], SimpleTreeNode(12, None))

    return st


@pytest.fixture
def st4():
    st = SimpleTree(None)
    st.AddChild(None, SimpleTreeNode(1, None))
    st.AddChild(st.Root, SimpleTreeNode(2, None))
    st.AddChild(st.Root.Children[0], SimpleTreeNode(5, None))
    st.AddChild(st.Root, SimpleTreeNode(3, None))
    st.AddChild(st.Root.Children[1], SimpleTreeNode(7, None))
    st.AddChild(st.Root, SimpleTreeNode(6, None))
    return st


def test_EvenTrees(st, st4):
    assert len(st.EvenTrees()) == 6
    assert len(st4.EvenTrees()) == 4
