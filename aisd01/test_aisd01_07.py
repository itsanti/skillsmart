import pytest
from aisd01_07 import OrderedList, OrderedStringList


@pytest.fixture
def olist():
    olist = OrderedList(True)
    return olist


@pytest.fixture
def oliststring():
    oliststring = OrderedStringList(True)
    return oliststring


def test_compare_string(oliststring):
    assert oliststring.compare(' a', 'b') == -1
    assert oliststring.compare('a ', ' a') == 0
    assert oliststring.compare('b', 'a') == 1


def test_add_string(oliststring):
    oliststring.add('aa')
    oliststring.add('ab')
    print(oliststring.get_all())

    oliststring.clean(False)
    oliststring.add('aa')
    oliststring.add('ab')
    print(oliststring.get_all())


def test_compare(olist):
    assert olist.compare(3, 4) == -1
    assert olist.compare(4, 4) == 0
    assert olist.compare(5, 4) == 1


def test_add(olist):
    olist.add(2)
    olist.add(1)
    olist.add(3)
    olist.add(2)
    olist.add(4)
    print(olist.get_all())

    olist.clean(False)
    olist.add(3)
    olist.add(2)
    olist.add(4)
    olist.add(1)
    print(olist.get_all())


def test_find(olist):
    assert olist.find(3) is None
    olist.add(3)
    assert olist.find(3).value == 3
    olist.add(1)
    olist.add(5)
    assert olist.find(3).value == 3

    olist.clean(False)
    olist.add(1)
    olist.add(3)
    olist.add(5)
    assert olist.find(3).value == 3
    assert olist.find(1).value == 1


def test_delete(olist):
    olist.add(3)
    olist.add(2)
    olist.delete(3)
    print(olist.get_all())
    olist.delete(2)
    assert olist.delete(3) is None


def test_clean(olist):
    olist.clean(False)
    assert olist.len() == 0


def test_len(olist):
    assert olist.len() == 0
    olist.add(1)
    olist.add(2)
    assert olist.len() == 2


def test_get_all(olist):
    assert olist.get_all() == []
    olist.add(2)
    assert olist.get_all()[0].value == 2
