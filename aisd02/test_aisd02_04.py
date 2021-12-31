import pytest
from aisd02_04_BST_array import *


@pytest.fixture
def bst() -> aBST:
    bst = aBST(1)
    return bst


def test_FindKeyIndex(bst: aBST):
    assert bst.FindKeyIndex(1) == 0
    bst.AddKey(4)
    bst.AddKey(2)
    assert bst.FindKeyIndex(5) == -2
    bst.AddKey(5)
    assert bst.FindKeyIndex(4) == 0
    assert bst.FindKeyIndex(2) == 1
    assert bst.FindKeyIndex(5) == 2
    assert bst.FindKeyIndex(6) is None


def test_AddKey(bst):
    assert bst.AddKey(4) == 0
    assert bst.AddKey(2) == 1
    assert bst.AddKey(2) == 1
    assert bst.AddKey(5) == 2
    assert bst.AddKey(1) == -1
    assert bst.AddKey(3) == -1
    assert bst.Tree == [4, 2, 5]
