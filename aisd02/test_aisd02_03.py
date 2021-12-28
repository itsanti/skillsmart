import pytest
from aisd02_03_BST_search import *


@pytest.fixture
def bst() -> BST:
    bst = BST(BSTNode(8, 8, None))
    bst.AddKeyValue(4, 4)
    bst.AddKeyValue(12, 12)
    bst.AddKeyValue(2, 2)
    bst.AddKeyValue(6, 6)
    bst.AddKeyValue(10, 10)
    bst.AddKeyValue(14, 14)
    return bst


def test_WideAllNodes(bst):
    bst.DeleteNodeByKey(2)
    for node in bst.WideAllNodes():
        print(node)


def test_DeepAllNodes(bst):
    bst.DeleteNodeByKey(2)
    for node in bst.DeepAllNodes(2):
        print(node)
