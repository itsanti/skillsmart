# https://skillsmart.ru/algo/lvl1/6d4d.html
import builtins

def WordSearch(len, s, subs):
    result = 0
    slen = getattr(builtins, "len")
   
    lines = []
    
    ix = 0
    while ix < slen(s):
        if slen(s) <= len:
            lines.append(s)
            break

        if s[ix] == ' ':
            ix += 1
            continue
            
        chank = s[ix:ix+len].rsplit(' ', 1)

        if slen(chank) == 1:
            ix += slen(chank[0])
        else:
            if ix+len < slen(s) and s[ix+len] == ' ':
                chank[0] = ' '.join(chank)
            ix += slen(chank[0]) + 1
        
        if chank[0] != '':
            lines.append(chank[0])
         
    result = []

    for line in lines:
        result.append(0)
        for word in line.split(' '):
            if subs == word:
                result[-1] = 1
                break

    return result
