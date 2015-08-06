N = input()
if not('0' in N or '2' in N or '4' in N or '6' in N or '8' in N):
    print(-1)
    exit()
smalls = [i for i in '02468'[:(int(N[-1])+1)//2]]
bigs = [i for i in '02468'[(int(N[-1])+1)//2:]]

for i in range(len(N)):
    if N[i] in smalls:
        N = N[:i]+N[-1]+N[i+1:-1]+N[i]
        print(N)
        exit()
for i in range(len(N))[::-1]:
    if N[i] in bigs:
        N = N[:i]+N[-1]+N[i+1:-1]+N[i]
        print(N)
        exit()