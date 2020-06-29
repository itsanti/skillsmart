# https://skillsmart.ru/algo/lvl1/3b3d.html

def UFO(N, data, octal):
    base = 8 if octal else 16
    return [int(str(x), base) for x in data]
