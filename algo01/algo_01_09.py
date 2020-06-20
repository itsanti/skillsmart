# https://skillsmart.ru/algo/lvl1/l1e7.html

def PrintingCosts(Line):
    map = {
        ' ': 0, "`'" : 3, '.': 4, '"': 6, ',-^': 7, ':_': 8, '!~': 9, '>\\/<': 10, ';': 11,
        '(|)': 12, 'vrx+': 13, 'Y=': 14, '?i': 15, 'LlT7': 16, 'tcu*': 17, 'JXnfI{}[]': 18,
        'Vzw1': 19, 'ojFC': 20, 'hKk4s': 21, '20Z%m': 22, '8P3eUa': 23, '&#Ay' : 24, 'bdpqGSHN': 25,
        'D9EW6O': 26, '5': 27, 'RM': 28, 'B$': 29, 'g': 30, 'Q': 31, '@': 32, 'def': 23
    }
    
    volume = 0
    
    for char in Line:
        for key in map.keys():
            if char in key:
                volume += map.get(key)
                break
        else:
            volume += map.get('def')
        
    return volume
