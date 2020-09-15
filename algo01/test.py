from algo_01_23 import BalancedParentheses

td = [
    ['()', 1],
    ['(()) ()()', 2],
    ['((())) (()()) (())() ()(()) ()()()', 3],
]

for e in td:
    print(f'BalancedParentheses: \'{e[0]}\': |{BalancedParentheses(*e[1:])}|')
