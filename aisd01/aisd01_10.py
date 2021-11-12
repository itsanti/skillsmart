
class PowerSet:

    def __init__(self):
        # ваша реализация хранилища
        self.values = []

    def size(self):
        # количество элементов в множестве
        return len(self.values)

    def put(self, value):
        # всегда срабатывает
        if value not in self.values:
            self.values.append(value)

    def get(self, value):
        # возвращает True если value имеется в множестве,
        # иначе False
        return value in self.values

    def remove(self, value):
        # возвращает True если value удалено
        # иначе False
        if value in self.values:
            self.values.remove(value)
            return True
        return False

    def intersection(self, set2):
        set2: PowerSet
        # пересечение текущего множества и set2
        if self.size() == 0 or set2.size() == 0:
            return PowerSet()

        result = PowerSet()
        iter_set = self.values if self.size() <= set2.size() else set2.values
        target_set = self.values if self.values is not iter_set else set2.values

        for element in iter_set:
            if element in target_set:
                result.put(element)

        return result

    def union(self, set2):
        # объединение текущего множества и set2
        intersection = self.intersection(set2)

        union_set = PowerSet()
        union_set.values = self.values.copy()
        union_set.values.extend(set2.values)

        if intersection.size() > 0:
            for element in intersection.values:
                union_set.remove(element)

        return union_set

    def difference(self, set2):
        # разница текущего множества и set2
        result = PowerSet()
        if self.size() == 0:
            return result
        elif set2.size() == 0:
            result.values = self.values.copy()
            return result

        for element in self.values:
            if element not in set2.values:
                result.values.append(element)

        return result

    def issubset(self, set2):
        # возвращает True, если set2 есть
        # подмножество текущего множества,
        # иначе False
        if set2.size() == 0:
            return True

        for element in set2.values:
            if element not in self.values:
                return False

        return True
