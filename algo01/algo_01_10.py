# https://skillsmart.ru/algo/lvl1/s81f.html

def BigMinus(s1, s2):
    if s1 == '0' or s2 == '0':
        return s1 if s2 == '0' else s2
        
    s1l = len(s1)
    s2l = len(s2)
    
    if s1l != s2l:
        if s1l > s2l:
            s2 = '0' * (s1l - s2l) + s2
        else:
            s1 = '0' * (s2l - s1l) + s1

    for ix in range(len(s1)):
        if int(s1[ix]) < int(s2[ix]):
            s1, s2 = s2, s1
            break
        elif int(s1[ix]) > int(s2[ix]):
            break
    else:
        return '0'
        
    c = 0
    result = ''
    for ix in range(len(s1) - 1, -1, -1):
        a = int(s1[ix])
        b = int(s2[ix])
        if c > 0:
            a -= 1
            c = 0
        if a < b:
            c = 10
        result = str(a + c - b) + result

    if len(result) > 1 and result[0] == '0':
        ix = 0
        while result[ix] == '0' and ix < len(result) - 1:
            ix += 1
        result = result[ix:]
        
    return result

