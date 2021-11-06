import pytest
from aisd01_08 import HashTable


@pytest.fixture
def ht():
    return HashTable(17, 3)


def test_hash_fun(ht):
    assert ht.hash_fun('aaa') == ht.hash_fun('aaa')
    assert ht.hash_fun('aaa') != ht.hash_fun('aa')
    assert ht.hash_fun('aab') == ht.hash_fun('aab')
    print(ht.hash_fun('aaa'))
    print(ht.hash_fun('aa'))
    print(ht.hash_fun('aab'))


def test_seek_slot(ht):
    assert ht.seek_slot('aaa') == 7
    assert ht.seek_slot('aa') == 15
    assert ht.seek_slot('aab') == 16
    assert ht.seek_slot('aab') == 16


def test_put(ht):
    print(ht.put(''))
    print(ht.put(''))
    assert ht.put('aaa') == 7
    assert ht.put('aaa') == 7
    assert ht.put('aa') == 15
    assert ht.put('aab') == 16


def test_find(ht):
    ht.put('aaa b')
    assert ht.find('aaa b') == 10
    assert ht.find('a') is None
