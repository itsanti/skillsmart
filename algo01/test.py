from algo_01_12 import UFO

td = [
    ['4660,6007', 2, [1234, 1777], False],
    ['668,1023', 2, [1234, 1777], True],
    ['16,17,18', 3, [10, 11, 12], False] 
]

for e in td:
    print(f'UFO: {e[0]}: {UFO(*e[1:])}')
