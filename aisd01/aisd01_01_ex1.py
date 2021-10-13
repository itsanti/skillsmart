'''
Напишите функцию, которая получает на вход два связанных списка, состоящие из целых значений,
и если их длины равны, возвращает список, каждый элемент которого равен сумме соответствующих элементов входных списков.
'''

from aisd01_01 import LinkedList, Node


def linked_sum(list1: LinkedList, list2: LinkedList):
    if list1.len() == list2.len():
        result = LinkedList()
        node1 = list1.head
        node2 = list2.head
        while node1 is not None:
            result.add_in_tail(Node(node1.value + node2.value))
            node1 = node1.next
            node2 = node2.next
        return result
    return None
