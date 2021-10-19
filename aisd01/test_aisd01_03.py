import pytest
from aisd01_03 import DynArray


@pytest.fixture
def da():
    da = DynArray()
    for i in range(15):
        da.append(i)
    return da


def test_delete(da):
    before_capacity = da.capacity
    da.delete(0)
    assert da[0] == 1
    assert len(da) == 14
    assert before_capacity == da.capacity

    with pytest.raises(IndexError):
        da.delete(98)

    da.insert(0, 1)
    da.insert(0, 1)
    da.insert(0, 1)
    assert da.capacity == 32

    da.delete(4)
    assert da.capacity == 32
    da.delete(4)
    assert da.capacity == 21


def test_insert(da):
    before_capacity = da.capacity

    da.insert(0, 13)
    assert da[0] == 13
    assert da[5] == 4
    assert da.capacity == before_capacity

    da.insert(0, 14)
    assert da[0] == 14
    assert da[1] == 13
    assert da.capacity == 2 * before_capacity

    with pytest.raises(IndexError):
        da.insert(30, 15)

    da.insert(17, 23)
    assert da[17] == 23
