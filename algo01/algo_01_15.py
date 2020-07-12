# https://skillsmart.ru/algo/lvl1/d146.html

# string line

def LineAnalysis(line):
    dots = line.count('.')
    stars = len(line) - dots
    if dots == 0 or stars == 2:
        return True
    gdots = 0
    for char in line[1:]:
        if char == '*':
            break
        gdots += 1
    return gdots * (stars - 1) == dots
