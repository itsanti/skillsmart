# https://skillsmart.ru/algo/lvl1/b519.html

# string [] ShopOLAP(int N, string [] items)

def ShopOLAP(N, items):
    if N == 1:
        return items
    
    orders = {}
    for item in items:
        el = item.split(' ')
        if el[0] not in orders:
            orders[el[0]] = int(el[1])
        else:
            orders[el[0]] += int(el[1])
                      
    sort_orders = sorted(orders.items(), key=lambda x: x[1], reverse=True)
    sort_orders.append(('', -1))
    
    result = []
    start = 0
    end = start + 1
    for x in range(0, len(sort_orders) - 1):
        if sort_orders[x + 1][1] == sort_orders[x][1]:
           end = x + 2
        else:
            result.extend(sorted(sort_orders[start:end], key=lambda x: x[0]))
            start = x + 1
            end = start + 1
    
    return list(map(lambda e: e[0] + ' ' + str(e[1]), result))
