# https://skillsmart.ru/algo/lvl1/oafd.html

# boolean Football(int F[], int N)


def Football(F, N):
    if N == 1:
        return True
    if N == 2:
        return F[0] > F[1]
    
    six = search_siq(F)
    if None in six:
        return False
    if (six[1] - six[0]) + 1 == len(F):
        return True
    
    lcheck = F[:six[0]] + F[six[0]:six[1]+1][::-1] + F[six[1]+1:]
    return check_sorted(lcheck)


def search_siq(a):
    sp = [None, None]
    for ix, e in enumerate(a[:-1]):
        if a[ix] > a[ix + 1] and sp[0] is None:
            sp[0] = ix
            sp[1] = ix + 1
        elif a[ix] > a[ix + 1]:
            sp[1] = ix + 1
        elif a[ix] < a[ix + 1] and sp[0] is not None:
            return sp
    return sp


def check_sorted(a):
    flag = True
    i = 1
    while i < len(a): 
        if(a[i] < a[i - 1]): 
            flag = False
        i += 1
    return flag
