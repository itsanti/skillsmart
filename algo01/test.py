from algo_01_15 import LineAnalysis

td = [
    ['True', '*..*..*..*..*..*..*'],
    ['True', '*'],
    ['True', '***'],
    ['True', '*.......*.......*'],
    ['True', '**'],
    ['True', '*.*'],
    ['False', '*..*...*..*..*..*..*'],
    ['False', '*..*..*..*..*..**..*'],
    ['False', '*...*..*..*'],
]

for e in td:
    print(f'LineAnalysis: {e[0]}: {LineAnalysis(*e[1:])}')

