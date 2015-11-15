N=int(input())
C=[int(input()) for i in range(N)]

divs = [[C[i]%C[j]==0 for j in range(N)] for i in range(N)]
for i in range(N):
    divs[i][i] = False

e = 0
for i in range(N):
    cnt = divs[i].count(True)
    if cnt%2==0:
        e += (cnt+2)/(2*cnt+2)
    else:
        e += 1/2
print(e)
