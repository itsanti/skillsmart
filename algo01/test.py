from algo_01_11 import MassVote

td = [
    ['majority winner 1', 5, [60, 10, 10, 15, 5]], # Победил первый кандидат с результатом 60%
    ['minority winner 2', 3, [10, 15, 10]], # Победил второй кандидат с результатом 42.85%.
    ['no winner', 4, [111, 111, 110, 110]], # Перевыборы
    
    ['majority winner 1', 1, [60]],
    ['no winner', 2, [2, 2]],
    ['minority winner 6', 7, [2, 2, 43, 1, 43, 54, 1]],
    ['majority winner 6', 7, [2, 2, 43, 1, 43, 154, 1]]
]

for e in td:
    print(f'MassVote: {e[0]}: {MassVote(*e[1:])}')
