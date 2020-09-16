# https://skillsmart.ru/algo/lvl1/oo0b.html

# string Keymaker(int k)


def Keymaker(k):
    if k == 1:
        return '1'
    doors = [True]*k
    n = 2
    while n < k:
        for ix in range(n - 1, k, n):
            doors[ix] = not doors[ix]
        n += 1
    doors[-1] = not doors[-1]
    return ''.join([str(int(door)) for door in doors])
