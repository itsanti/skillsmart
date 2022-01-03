import pytest
from aisd02_06_BalancedBST import *


@pytest.fixture
def bst():
    return BalancedBST()


def test_GenerateTree(bst):
    bst.GenerateTree([])
    assert bst.Root is None
    bst.GenerateTree([3])
    assert bst.Root.NodeKey == 3
    bst.GenerateTree([4, 5, 2])
    assert bst.Root.NodeKey == 4
    assert bst.Root.LeftChild.NodeKey == 2
    assert bst.Root.RightChild.NodeKey == 5


def test_IsBalanced(bst):
    assert bst.IsBalanced(bst.Root)
    bst.GenerateTree([4, 5, 2])
    assert bst.IsBalanced(bst.Root)
    bst.GenerateTree([29, 3, 7, 9, 5, 5, 20, 4, 33, 26, 28, 0, 26])
    assert bst.IsBalanced(bst.Root)
