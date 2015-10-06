import math
X=int(input())
Y=int(input())
L=int(input())
total = math.ceil(abs(Y)/L)
total += math.ceil(abs(X)/L)
if Y<0:
    total += 2
elif X != 0:
    total += 1
print(total)
