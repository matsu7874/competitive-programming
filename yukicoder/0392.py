def get_route(n):
    route = []
    while n>1:
        if n & 1:
            route.append('R')
        else:
            route.append('L')
        n >>= 1
    return reversed(route)

n = int(input())

for i in range(n):
    a = int(input())
    print(''.join(get_route(a+1)))