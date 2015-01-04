n = int(input())
i = 1
B = []
while 2**(i-1) <= n:
    B.append(n%(2**i)//(2**(i-1)))
    i += 1
if B == B[::-1]:
    print('Yes')
else:
    print('No')