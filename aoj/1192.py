def after_tax_price(tax_rate, before_tax_price):
    return before_tax_price*(100+tax_rate)//100

def max_before_tax_price(tax_rate, after_tax_price):
    a = after_tax_price*100/(100+tax_rate)
    if int(a) < a:
        return int(a)+1
    else:
        return int(a)
while True:
    (x, y, s) = [int(x) for x in input().split()]
    if x==0 and y==0 and s==0:
        exit()
    max_price = 0
    for i in range(1, s//2+1):
        price = after_tax_price(y,max_before_tax_price(x,i))+after_tax_price(y,max_before_tax_price(x,s-i))
        if price>max_price
            max_price = max(max_price, price)
    print(max_price)
