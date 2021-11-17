class BloomFilter:

    def __init__(self, f_len):
        self.filter_len = f_len
        # создаём битовый массив длиной f_len ...
        self.bitarray = 0

    def hash1(self, str1):
        rnd = 17
        code = 0
        for c in str1:
            code = (code * rnd + ord(c)) % self.filter_len
        return code

    def hash2(self, str1):
        rnd = 223
        code = 0
        for c in str1:
            code = (code * rnd + ord(c)) % self.filter_len
        return code

    def add(self, str1):
        self.bitarray |= self.hash1(str1) | self.hash2(str1)

    def is_value(self, str1):
        # проверка, имеется ли строка str1 в фильтре
        mask = self.hash1(str1) | self.hash2(str1)
        return mask == self.bitarray & mask
