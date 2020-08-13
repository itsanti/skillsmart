# https://skillsmart.ru/algo/lvl1/b7de.html

# boolean SherlockValidString(string s)

def SherlockValidString(s):
    if len(s) < 2:
        return True
        
    map = {}
    for char in s:
        if char in map:
            continue
        else:
            map[char] = s.count(char)
    code = list(map.values())
    
    for (ix, el) in enumerate(code):
        subl = code[:ix]+code[ix+1:]
        if el != 1:
            subl.append(el - 1)
        if sum(subl) / len(subl) == max(subl):
            return True
    return False
