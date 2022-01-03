import pytest
from aisd02_05_GenerateBBSTArray import *


@pytest.fixture
def arr():
    return [4, 5, 2]


def test_GenerateBBSTArray(arr):
    assert GenerateBBSTArray(arr) == [4, 2, 5]
    assert GenerateBBSTArray([4, 5, 2, 1]) == [4, 2, 5, 1, None, None, None]
    assert GenerateBBSTArray([]) == [None]
    assert GenerateBBSTArray([29, 3, 7, 9, 5, 5, 20, 4, 33, 26, 28, 0, 26]) \
           == [9, 5, 28, 3, 7, 26, 33, 0, 4, 5, None, 20, 26, 29, None]

