import math
n=int(input())
a=list(map(int, input().split()))
ave = sum(a)/n
if math.ceil(ave)-ave > ave-math.floor(ave):
    t = math.floor(ave)
else:
    t = math.ceil(ave)
total = 0
for v in a:
    total += (t-v) ** 2
print(total)