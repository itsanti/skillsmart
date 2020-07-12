# https://skillsmart.ru/algo/lvl1/beea.html

# int N
# int [] price

def MaximumDiscount(N, price):
    if N < 3:
        return 0
    price.sort(reverse=True)
    discount = 0
    for chank in range(N // 3):
        discount += price[3*chank:3*(chank+1)][-1]
    return discount
