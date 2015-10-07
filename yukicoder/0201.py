S, P, X = input().split()
s, p, x = input().split()
P = int(P)
p = int(p)
if P > p:
    print(S)
elif P < p:
    print(s)
else:
    print(-1)
