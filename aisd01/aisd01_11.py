class BloomFilter:

    def __init__(self, f_len):
        self.filter_len = f_len
        # создаём битовый массив длиной f_len ...
        self.bitarray = [0] * self.filter_len

    def hash1(self, str1):
        rnd = 17
        code = 0
        for c in str1:
            code = (code * rnd + ord(c)) % self.filter_len
        return 2 ** (self.filter_len - code % self.filter_len - 1)

    def hash2(self, str1):
        rnd = 223
        code = 0
        for c in str1:
            code = (code * rnd + ord(c)) % self.filter_len
        return 2 ** (self.filter_len - code % self.filter_len - 1)

    def add(self, str1):
        hash1_mask = bin(self.hash1(str1))[2:].zfill(self.filter_len).index('1')
        hash2_mask = bin(self.hash2(str1))[2:].zfill(self.filter_len).index('1')
        self.bitarray[hash1_mask] = 1
        self.bitarray[hash2_mask] = 1

    def is_value(self, str1):
        # проверка, имеется ли строка str1 в фильтре
        hash1_mask = self.hash1(str1)
        hash2_mask = self.hash2(str1)
        total_mask = hash1_mask | hash2_mask
        bit_mask = int(''.join(map(str, self.bitarray)), 2)
        return total_mask == bit_mask & total_mask
