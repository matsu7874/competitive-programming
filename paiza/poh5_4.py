X,Y,N = [int(x) for x in input().split()]
T = []
for i in range(Y):
    t = [int(x) for x in input().split()]
    T.extend(t)
CT = [False for i in range(X*Y)]
for n in range(N):
    xs,ys,xe,ye = [int(x) for x in input().split()]
    for yt in range(ys-1,ye):
        for xt in range(xs-1,xe):
            CT[xt+yt*X] = True

point = 0
for i in range(Y):
    for j in range(X):
        if CT[j+i*X] == True:
            point += T[j+i*X]
print(point)