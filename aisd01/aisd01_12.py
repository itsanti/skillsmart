class NativeCache:
    def __init__(self, sz):
        self.size = sz
        self.slots = [None] * self.size
        self.values = [None] * self.size
        self.hits = [0] * self.size
        self._step = 3

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

    def seek_slot(self, key):
        # находит индекс пустого слота для значения, или None
        slot = self.hash_fun(key)
        if self.slots[slot] is not None and key != self.slots[slot]:
            start_seek = slot
            is_end = False
            while self.slots[slot] is not None:
                slot = (slot + self._step) % self.size
                if slot <= start_seek:
                    is_end = True
                if is_end and slot >= start_seek:
                    return None
        return slot

    def is_key(self, key):
        # возвращает True если ключ имеется,
        # иначе False
        if key in self.slots:
            self.hits[self.slots.index(key)] += 1
            return True
        return False

    def put(self, key, value):
        # записываем значение по хэш-функции
        # возвращается индекс слота
        slot = self.seek_slot(key)
        if slot is None:
            slot = self.seek_min_slot()
            self.hits[slot] = 0

        self.slots[slot] = key
        self.values[slot] = value
        return slot

    def get(self, key):
        # возвращает value для key,
        # или None если ключ не найден
        if self.is_key(key):
            return self.values[self.slots.index(key)]
        return None

    def seek_min_slot(self):
        return self.hits.index(min(self.hits))
