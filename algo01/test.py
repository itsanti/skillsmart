from algo_01_06 import WordSearch


len = 1
s = 'sd ssd'
subs = 'd'
print(f'WordSearch: {WordSearch(len, s, subs)}')

len = 12
s = 'строка разбивается на набор строк через выравнивание по заданной ширине.'
subs = 'строк'
print(f'WordSearch: {WordSearch(len, s, subs)}')


