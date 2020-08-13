from algo_01_18 import BiggerGreater

td = [
    ['', 'а'],
    ['аz', 'zа'],
    ['яа', 'ая'],
    ['', 'fff'],
    ['нкмл', 'нклм'],
    ['викб', 'вибк'],
    ['ибвк', 'вкиб'],
]

for e in td:
    print(f'BiggerGreater: \'{e[0]}\': {BiggerGreater(*e[1:])}')
