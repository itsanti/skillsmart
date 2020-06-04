import math

def squirrel(N):
    factorial = 1
    while (N > 1):
        factorial *= N
        N -= 1
    return factorial // 10 ** int(math.log(factorial, 10))
