F = [0 for x in range(10000000)]
def functional(n):
    print(n)
    if F[n] != 0:
        return F[n]
    elif n>1:
        F[n] = n*functional(n-1)
        return F[n]
    else:
        return 1

print('F = [',end='')
for i in range(20001):
    print(functional(i),',',end='')
print(']')
