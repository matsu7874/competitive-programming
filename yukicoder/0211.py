K=int(input())
P=[0]*201
for a in [2,3,5,7,11,13]:
    for b in [4,6,8,9,10,12]:
        P[a*b] += 1/36
print(P[K])
