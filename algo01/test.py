from algo_01_24 import Football

td = [
    ['5 - True', [5], 1],
    ['3 4 - False', [3, 4], 2],
    ['4 3 - True', [4, 3], 2],
    ['1 2 3 - False', [1, 2, 3], 3],
    ['1 3 2 - True', [1, 3, 2], 3],
    ['3 2 1 - True', [3, 2, 1], 3],
    ['1 7 5 3 9 - True', [1, 7, 5, 3, 9], 5],
    ['9 5 3 7 1 - False', [9, 5, 3, 7, 1], 5],
    ['1 4 3 2 5 - True', [1, 4, 3, 2, 5], 5],
]

for e in td:
    print(f'Football: \'{e[0]}\': |{Football(*e[1:])}|')
