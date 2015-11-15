N=int(input())
C = input().split()
C.sort()
num = []
op = []
for c in C:
    if c in '+-':
        op.append(c)
    else:
        num.append(int(c))
print(op,num)
