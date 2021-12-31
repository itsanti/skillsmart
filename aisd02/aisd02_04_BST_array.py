class aBST:

    def __init__(self, depth):
        # правильно рассчитайте размер массива для дерева глубины depth:
        tree_size = 2 ** (depth + 1) - 1
        self.Tree = [None] * tree_size  # массив ключей

    def FindKeyIndex(self, key):
        i = 0
        while i < len(self.Tree):
            if self.Tree[i] is None:
                return -i
            if self.Tree[i] == key:
                return i
            elif key < self.Tree[i]:
                i = 2 * i + 1
            elif key > self.Tree[i]:
                i = 2 * i + 2
        return None  # не найден

    def AddKey(self, key):
        i = self.FindKeyIndex(key)
        if i is not None:
            if i <= 0:
                index = -i
                self.Tree[index] = key
                return index
            else:
                return i
        return -1
