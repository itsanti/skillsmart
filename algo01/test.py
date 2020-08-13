from algo_01_19 import SherlockValidString

td = [
    ['x', 'x'],
    ['True', 'xx'],
    ['True', 'xz'],
    ['True', 'xyz'],
    ['True', 'xxz'],
    ['True', 'xyzaa'],
    ['True', 'xxyyz'],
    ['False', 'xyzzz'],
    ['False', 'xxyyza'],
    ['False', 'xxyyzabc'],
    ['True', 'xxxxxyyyyy'],
]

for e in td:
    print(f'SherlockValidString: \'{e[0]}\': {SherlockValidString(*e[1:])}')
