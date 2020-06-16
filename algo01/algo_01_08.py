# https://skillsmart.ru/algo/lvl1/ab53.html

def TheRabbitsFoot(s, encode):
    if encode:
        s = ''.join(s.split())
        dim_x = int(len(s) ** 0.5)
        dim_y = dim_x + 1
        if dim_x * dim_y < len(s):
            dim_x += 1
        result = []
        for ix in range(dim_y):
            stmp = ''
            for char in range(ix, len(s), dim_y):
                stmp += s[char]
            result.append(stmp)
        result = ' '.join(result)
        return result
    
    s = [list(x) for x in s.split()]
    wl = len(s[0])
    for ix in range(len(s)):
        if len(s[ix]) < wl:
            s[ix] = s[ix] + [''] * (wl - len(s[ix]))
    return ''.join([''.join(chank) for chank in zip(*s)])
