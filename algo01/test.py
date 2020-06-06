from algo_01_05 import PatternUnlock

N = 1
hits = [5]
print(f'unblock "": {PatternUnlock(N, hits)}')

N = 2
hits = [5, 3]
print(f'unblock "141421": {PatternUnlock(N, hits)}')

N = 7
hits = [2,6,5,2,9,1,6]
print(f'unblock "682843": {PatternUnlock(N, hits)}')

N = 9
hits = [6,2,9,1,5,3,8,1,5]
print(f'unblock "189949": {PatternUnlock(N, hits)}')

N = 10
hits = [1,2,3,4,5,6,2,7,8,9]
print(f'unblock "982843": {PatternUnlock(N, hits)}')
