from algo_01_14 import MaximumDiscount

td = [
    ['450', 7, [400, 350, 300, 250, 200, 150, 100]],
    ['3', 5, [1,2,3,4,5]],
    ['0', 2, [1,2]],
    ['1', 3, [1,2,4]],
]

for e in td:
    print(f'MaximumDiscount: {e[0]}: {MaximumDiscount(*e[1:])}')


