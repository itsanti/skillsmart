import pytest
from aisd01_10 import PowerSet


@pytest.fixture
def ps():
    return PowerSet()


def test_size(ps):
    assert ps.size() == 0
    ps.put(1)
    assert ps.size() == 1
    ps.remove(1)
    assert ps.size() == 0


def test_put(ps):
    ps.put(12)
    assert ps.values[0] == 12
    ps.put(12)
    assert ps.size() == 1
    ps.put(13)
    assert ps.values[1] == 13
    assert ps.size() == 2


def test_get(ps):
    ps.put(12)
    assert ps.get(12) is True
    assert ps.get(13) is False


def test_remove(ps):
    assert ps.remove(12) is False
    ps.put(12)
    assert ps.remove(12) is True
    assert ps.size() == 0


def test_intersection(ps):
    a = PowerSet()
    b = PowerSet()
    a.put(1)
    assert ps.intersection(a).size() == 0
    assert ps.intersection(ps).size() == 0
    ps.put(2)
    assert ps.intersection(b).size() == 0
    assert ps.intersection(a).size() == 0
    b.put(2)
    assert ps.intersection(b).size() == 1
    ps.put(3)
    ps.put(4)
    b.put(4)
    assert ps.intersection(b).size() == 2
    print(ps.intersection(b).values)


def test_union(ps):
    a = PowerSet()
    a.put(23)
    a.put(13)

    assert ps.union(ps).size() == 0
    assert ps.union(a).size() == 2
    ps.put(10)
    assert ps.union(a).size() == 3
    ps.put(13)
    assert ps.union(a).size() == 3


def test_difference(ps):
    a = PowerSet()
    a.put(12)
    assert ps.difference(ps).size() == 0
    assert ps.difference(a).size() == 0
    ps.put(13)
    ps.put(14)
    assert ps.difference(PowerSet()).size() == 2

    ps.put(12)
    assert ps.difference(a).size() == 2


def test_issubset(ps):
    a = PowerSet()
    a.put(11)
    assert ps.issubset(ps) is True
    assert a.issubset(ps) is True
    assert ps.issubset(a) is False
    a.put(12)
    ps.put(11)
    assert ps.issubset(a) is False
    ps.put(12)
    assert ps.issubset(a) is True
    ps.put(13)
    assert ps.issubset(a) is True


def test_hiload(ps):
    c, d = PowerSet(), PowerSet()
    c.values = [i for i in range(20000)]
    d.values = [i for i in range(1000)]
    assert c.union(d).size() == 20000
    d.values = [i for i in range(20001, 21001)]
    assert c.union(d).size() == 21000
