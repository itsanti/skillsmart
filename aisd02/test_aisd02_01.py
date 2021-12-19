import pytest
from aisd02_01_SimpleTree import SimpleTreeNode, SimpleTree


@pytest.fixture
def st():
    st = SimpleTree(None)
    st.AddChild(None, SimpleTreeNode(9, None))
    st.AddChild(st.Root, SimpleTreeNode(4, None))
    return st


def test_AddChild(st):
    st.AddChild(st.Root.Children[0], SimpleTreeNode(6, None))
    st.AddChild(st.Root, SimpleTreeNode(17, None))
    assert st.Root.Children[0].NodeValue == 4
    assert st.Root.Children[1].NodeValue == 17


def test_DeleteNode(st):
    st.AddChild(st.Root.Children[0], SimpleTreeNode(6, None))
    st.DeleteNode(st.Root.Children[0])
    assert len(st.Root.Children) == 0

def test_GetAllNodes(st):
    st.AddChild(st.Root.Children[0], SimpleTreeNode(6, None))
    st.AddChild(st.Root, SimpleTreeNode(17, None))
    assert [9, 4, 17, 6] == [node.NodeValue for node in st.GetAllNodes()]

    st = SimpleTree(None)
    assert [] == st.GetAllNodes()

    st.AddChild(None, SimpleTreeNode(9, None))
    assert [9] == [node.NodeValue for node in st.GetAllNodes()]

def test_FindNodesByValue(st):
    assert [] == st.FindNodesByValue(111)
    assert len(st.FindNodesByValue(9)) == 1
    st.AddChild(st.Root.Children[0], SimpleTreeNode(6, None))
    st.AddChild(st.Root.Children[0], SimpleTreeNode(6, None))
    assert len(st.FindNodesByValue(6)) == 2
    print([node.NodeValue for node in st.FindNodesByValue(6)])
    st.AddChild(st.Root, SimpleTreeNode(None, None))
    assert len(st.FindNodesByValue(None)) == 1

def test_MoveNode(st):
    st.MoveNode(st.Root.Children[0], st.Root)
    print([node.NodeValue for node in st.GetAllNodes()])
    st.AddChild(st.Root.Children[0], SimpleTreeNode(6, None))
    st.AddChild(st.Root, SimpleTreeNode(17, None))
    st.MoveNode(st.Root.Children[0], st.Root.Children[1])
    print([node.NodeValue for node in st.GetAllNodes()])

def test_Count(st):
    assert st.Count() == 2
    st.AddChild(st.Root, SimpleTreeNode(17, None))
    assert st.Count() == 3
    st = SimpleTree(None)
    assert st.Count() == 0

def test_LeafCount(st):
    assert st.LeafCount() == 1
    st.AddChild(st.Root, SimpleTreeNode(6, None))
    assert st.LeafCount() == 2
    st = SimpleTree(None)
    assert st.Count() == 0
    st.AddChild(None, SimpleTreeNode(9, None))
    assert st.LeafCount() == 1
