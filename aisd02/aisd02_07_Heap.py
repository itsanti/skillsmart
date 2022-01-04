class Heap:

    def __init__(self):
        self.HeapArray = []  # хранит неотрицательные числа-ключи

    def MakeHeap(self, a, depth):
        heap_size = 2 ** (depth + 1) - 1
        self.HeapArray = [None] * heap_size
        for el in a:
            self.Add(el)

    def GetMax(self):
        # вернуть значение корня и перестроить кучу
        if len(self.HeapArray) == 0 or len(self.HeapArray) == self.HeapArray.count(None):
            return -1
        elif len(self.HeapArray) < 3:
            return self.HeapArray.pop(0)
        max = self.HeapArray[0]
        if None in self.HeapArray:
            last_slot = self.HeapArray.index(None) - 1
        else:
            last_slot = len(self.HeapArray) - 1
        self.HeapArray[0] = self.HeapArray[last_slot]
        self.HeapArray[last_slot] = None

        index = 0
        while True:
            insert_slot = index
            left_child = index * 2 + 1
            right_child = index * 2 + 2

            if left_child < last_slot and self.HeapArray[left_child] > self.HeapArray[insert_slot]:
                insert_slot = left_child
            if right_child < last_slot and self.HeapArray[right_child] > self.HeapArray[insert_slot]:
                insert_slot = right_child
            if insert_slot == index:
                break

            self.HeapArray[index], self.HeapArray[insert_slot] = self.HeapArray[insert_slot], self.HeapArray[index]
            index = insert_slot
        return max

    def Add(self, key):
        if None not in self.HeapArray or len(self.HeapArray) == 0:
            return False
        else:
            insert_slot = self.HeapArray.index(None)
        self.HeapArray[insert_slot] = key

        parent_slot = (insert_slot - 1) // 2

        while insert_slot > 0 and parent_slot >= 0:
            if self.HeapArray[insert_slot] > self.HeapArray[parent_slot]:
                self.HeapArray[insert_slot], self.HeapArray[parent_slot] = \
                    self.HeapArray[parent_slot], self.HeapArray[insert_slot]
            insert_slot = parent_slot
            parent_slot = (insert_slot - 1) // 2

        return True
