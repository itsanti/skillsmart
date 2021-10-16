class Node:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None


class LinkedList2:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
            item.prev = None
            item.next = None
        else:
            self.tail.next = item
            item.prev = self.tail
        self.tail = item

    def add_in_head(self, newNode):
        if self.head is None:
            self.tail = newNode
            newNode.prev = None
            newNode.next = None
        else:
            newNode.next = self.head
            self.head.prev = newNode
        self.head = newNode

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
            if self.head is None:
                self.add_in_head(newNode)
            else:
                self.add_in_tail(newNode)
        elif afterNode == self.tail:
            self.add_in_tail(newNode)
        else:
            newNode.next = afterNode.next
            afterNode.next.prev = newNode
            afterNode.next = newNode
            newNode.prev = afterNode

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
                self.head.prev = None
        else:
            node = self.head.next
            while node is not None:
                if node.value == val:
                    if self.tail == node:
                        self.tail = self.tail.prev
                        self.tail.next = None
                    else:
                        node.prev.next = node.next
                        node.next.prev = node.prev
                    result = node
                    break
                node = node.next
        if all and result is not None:
            self.delete(val, True)
