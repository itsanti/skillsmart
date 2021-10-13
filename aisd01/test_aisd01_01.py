import pytest
from aisd01_01 import LinkedList, Node
from aisd01_01_ex1 import linked_sum

@pytest.fixture
def my_list():
    ll = LinkedList()
    ll.add_in_tail(Node(12))
    ll.add_in_tail(Node(55))
    return ll


def test_add_in_tail(my_list):
    my_list.add_in_tail(Node(13))

    assert my_list.tail.value == 13
    assert my_list.head.next.next == my_list.tail


def test_print_all_nodes(my_list):
    my_list.print_all_nodes()


def test_find(my_list):
    node = my_list.find(55)
    assert node.value == 55

    node = my_list.find(100)
    assert node is None


def test_find_all(my_list):
    my_list.add_in_tail(Node(55))
    assert len(my_list.find_all(55)) == 2
    assert len(my_list.find_all(13)) == 0
    assert len(my_list.find_all(12)) == 1


def test_delete(my_list):
    my_list.delete(12)
    assert my_list.find(12) is None

    my_list.add_in_tail(Node(13))
    my_list.delete(13)
    assert my_list.find(13) is None

    my_list.add_in_tail(Node(11))
    my_list.add_in_tail(Node(13))
    my_list.delete(11)
    assert my_list.find(11) is None
    my_list.delete(13)
    my_list.delete(55)
    my_list.delete(55)

    # check all=True
    my_list.add_in_tail(Node(13))
    my_list.add_in_tail(Node(13))
    my_list.add_in_tail(Node(11))
    my_list.delete(13, True)
    my_list.add_in_tail(Node(15))
    my_list.delete(11, True)

    # delete only one element
    my_list.clean()
    my_list.add_in_tail(Node(13))
    my_list.delete(13, True)
    my_list.print_all_nodes()


def test_clean(my_list):
    my_list.clean()
    assert my_list.head is None
    assert my_list.tail is None


def test_len(my_list):
    assert my_list.len() == 2
    my_list.add_in_tail(Node(11))
    assert my_list.len() == 3
    my_list.clean()
    assert my_list.len() == 0


def test_insert(my_list):
    my_list.insert(None, Node(42))
    afterNode = my_list.find(55)
    my_list.insert(afterNode, Node(56))
    my_list.insert(afterNode, Node(54))

    my_list.clean()
    my_list.insert(None, Node(42))
    my_list.insert(None, Node(43))
    my_list.print_all_nodes()


def test_linked_sum(my_list):
    my_list2 = LinkedList()
    assert linked_sum(my_list, my_list2) is None

    my_list2.add_in_tail(Node(1))
    my_list2.add_in_tail(Node(2))
    linked_sum(my_list, my_list2).print_all_nodes()
