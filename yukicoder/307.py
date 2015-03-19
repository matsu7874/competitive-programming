N,M = [int(x) for x in input().split()]
C = [int(x) for x in input().split()]
C.sort()
for i in range(N):
    M -= C[i]
#    print(i,C[i],M)
    if M<0:
        print(i)
        exit()
else:
    print(N)
