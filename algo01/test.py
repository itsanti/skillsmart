from algo_01_04 import SynchronizingTables

N = 3
ids = [50, 1, 1024]
salary = [20000, 100000, 90000]

print(f'salary [90000, 20000, 100000]: {SynchronizingTables(N, ids, salary)}')

N = 1
ids = [1]
salary = [20000]

print(f'salary [20000]: {SynchronizingTables(N, ids, salary)}')

N = 2
ids = [23, 1]
salary = [3, 20000]

print(f'salary [20000, 3]: {SynchronizingTables(N, ids, salary)}')
