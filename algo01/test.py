from algo_01_07 import SumOfThe

N = 2
data = [10, 11]
print(f'SumOfThe = None: {SumOfThe(N, data)}')

N = 2
data = [10, 10]
print(f'SumOfThe = 10: {SumOfThe(N, data)}')

N = 3
data = [0, 10, -10]
print(f'SumOfThe = 0: {SumOfThe(N, data)}')

N = 5
data = [10, -25, -45, -35, 5]
print(f'SumOfThe = -45: {SumOfThe(N, data)}')

N = 7
data = [100,-50, 10, -25, 90, -35, 90]
print(f'SumOfThe = 90: {SumOfThe(N, data)}')
