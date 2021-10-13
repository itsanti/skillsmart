class Node:

    def __init__(self, v):
        self.value = v
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
        else:
            self.tail.next = item
        self.tail = item

    def print_all_nodes(self):
        node = self.head
        while node is not None:
            print(node.value)
            node = node.next

    def find(self, val):
        node = self.head
        while node is not None:
            if node.value == val:
                return node
            node = node.next
        return None

    def find_all(self, val):
        result = []
        node = self.head
        while node is not None:
            if node.value == val:
                result.append(node)
            node = node.next
        return result

    def delete(self, val, all=False):
        result = None
        if self.head is None:
            return result
        if self.head.value == val:
            result = self.head
            self.head = self.head.next
            if self.head is None:
                self.tail = None
        else:
            node = self.head.next
            prev_node = self.head
            while node is not None:
                if node.value == val:
                    if self.tail == node:
                        self.tail = prev_node
                        self.tail.next = None
                    else:
                        prev_node.next = node.next
                    result = node
                    break
                prev_node = node
                node = node.next
        if all and result is not None:
            self.delete(val, True)

    def clean(self):
        self.__init__()

    def len(self):
        count = 0
        node = self.head
        while node is not None:
            count += 1
            node = node.next
        return count

    def insert(self, afterNode, newNode):
        if afterNode is None:
            newNode.next = self.head
            self.head = newNode
        elif afterNode == self.tail:
            self.add_in_tail(newNode)
        else:
            newNode.next = afterNode.next
            afterNode.next = newNode
