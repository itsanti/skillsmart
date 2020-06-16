from algo_01_08 import TheRabbitsFoot

s = 'На основании N вычисляется размер матрицы в которую будет упакован'
encode = True
print(f'TheRabbitsFoot: {TheRabbitsFoot(s, encode)}')

s = 'Ннсаротн аилзиру оиямцуп сNееыюа нвтрвбк оысмкуо вчяаодв аирттеа'
encode = False
print(f'TheRabbitsFoot: {TheRabbitsFoot(s, encode)}')

s = 'отдай мою кроличью лапку'
encode = True
print(f'TheRabbitsFoot = "омоюу толл дюиа акчп йрьк": {TheRabbitsFoot(s, encode)}')

s = "омоюу толл дюиа акчп йрьк"
encode = False
print(f'TheRabbitsFoot = "отдаймоюкроличьюлапку": {TheRabbitsFoot(s, encode)}')