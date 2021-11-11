import pytest
from aisd01_09 import NativeDictionary


@pytest.fixture
def nd():
    return NativeDictionary(17)


def test_hash_fun(nd):
    assert nd.hash_fun('a') == 1
    assert nd.hash_fun('aa') == 15
    assert nd.hash_fun('aaa') == 7


def test_is_key(nd):
    nd.put('b', 1)
    assert nd.is_key('a') is False
    assert nd.is_key('b') is True


def test_put(nd):
    nd.put('a', 23)
    nd.put('aaa', 17)
    assert nd.values[1] == 'a'
    assert nd.slots[1] == 23
    assert nd.values[7] == 'aaa'
    assert nd.slots[7] == 17
    nd.put('aaa', 12)
    assert nd.values[7] == 'aaa'
    assert nd.slots[7] == 12


def test_get(nd):
    nd.put('aa', 23)
    nd.put('aaa', 17)
    assert nd.get('') is None
    assert nd.get('a') is None
    assert nd.get('aa') == 23
    assert nd.get('aaa') == 17
