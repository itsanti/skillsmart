from algo_01_22 import TransformTransform

td = [
    ['False', [1, 2, 4], 3],
    ['True', [1,3], 2],
]

for e in td:
    print(f'TransformTransform: \'{e[0]}\': {TransformTransform(*e[1:])}')
