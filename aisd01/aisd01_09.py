class NativeDictionary:
    def __init__(self, sz):
        self.size = sz
        self.slots = [None] * self.size
        self.values = [None] * self.size

    def hash_fun(self, key):
        # в качестве key поступают строки!
        # всегда возвращает корректный индекс слота
        p = 31
        hash = 0
        p_pow = 1
        for char in key:
            hash += (ord(char) - ord('a') + 1) * p_pow
            p_pow *= p
        return hash % self.size

    def is_key(self, key):
        # возвращает True если ключ имеется,
        # иначе False
        return key in self.values

    def put(self, key, value):
        slot = self.hash_fun(key)
        self.slots[slot] = value
        self.values[slot] = key

    def get(self, key):
        # возвращает value для key,
        # или None если ключ не найден
        if self.is_key(key):
            return self.slots[self.values.index(key)]
        return None
