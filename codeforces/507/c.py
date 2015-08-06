import math
s = 'LRLRLRLRLRLRLRLRLRLRLRLRLRLRLRLRLRLRLRLRLRLRLRLRLRLRLRLRLRLRLRLRLRLRLRLRLRLRLRLRLRLRLRLRLRLRLRLRLRLRLRLRLRLRLRLRLRLRLRLRLRLRLRLRLRLRLRLRLRLRLRLRLRLRLRLRLRLRLRLRLRLRLRLRLRLRLRLRLRLRLRLRLRLRLRLRLRLRLRLR'
(h, n) = [int(x) for x in input().split()]
n = 2**(h)-1+n
left = 2**h
right = 2**(h+1)-1
path = []
for i in range(h):
    center = (right+left)/2
    if n>center:
        path.append('R')
        left = math.ceil(center)
    else:
        path.append('L')
        right = int(center)

cost = 1
for i in range(len(path)):
    if s[i] != path[i]:
        cost += 2**(h-i)-1+1
        s = s[:i]+s[i+1:]
    else:
        cost += 1
print(cost-1)
