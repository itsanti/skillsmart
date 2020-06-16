# https://skillsmart.ru/algo/lvl1/s60b.html

def SumOfThe(N, data):
    if N == 2 and data[0] == data [1]:
        return data[0]
    
    for it in range(N):
        last = data.pop()
        s = sum(data)
        if last == s:
            return last
        data.insert(0, last)
        
    return None
