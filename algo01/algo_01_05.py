def PatternUnlock(N, hits):
    if N < 2:
        return ''

    transition = {
        (1,2): 1, (1,5): 2 ** 0.5, (1,6): 1, (1,8): 2 ** 0.5, (1,9): 1,
        (2,3): 1, (2,4): 2 ** 0.5, (2,5): 1, (2,6): 2 ** 0.5,
        (2,7): 2 ** 0.5, (2,8): 1, (2,9): 2 ** 0.5,
        (3,4): 1, (3,5): 2 ** 0.5, (3,7): 1, (3,8): 2 ** 0.5,
        (4,5): 1, (5,6): 1, (7,8): 1, (8,9): 1
    }
    
    s = 0
    for hit in range(N - 1):
        key = (hits[hit], hits[hit + 1])
        if key[0] == key[1]: continue
        if key[0] > key[1]:
            key = (key[1], key[0])
        s += transition[key]
    
    result = ''
    for char in str(round(s, 5)):
        if char == '.' or char == '0':
            continue
        result += char
    
    return result
