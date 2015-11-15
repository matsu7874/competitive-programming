import itertools

def dis(a,b,x,y):
    return (a-x)*(a-x)+(b-y)*(b-y)

def boundary(X,Y):
    L = len(X)
    B = []
    oldpoint = X.index(max(X))
    B.append(oldpoint)
    vx = 1
    vy = 0
    while True:
        minpoint = oldpoint
        minvecx = 0
        minvecy = 0
        maxcos = -1
        for i in range(L):
            if i==oldpoint:
                continue
            ox =X[i]-X[oldpoint]
            oy =Y[i]-Y[oldpoint]
            cos = (ox*vx+oy*vy)/((ox*ox+oy*oy)**0.5)
            if cos > maxcos or (cos == maxcos and dis(X[oldpoint],Y[oldpoint],X[i],Y[i])<dis(X[oldpoint],Y[oldpoint],X[minpoint],Y[minpoint])):
                maxcos = cos
                minvecx = ox
                minvecy = oy
                minpoint = i
        if minpoint == B[0]:
            break
        vx = minvecx
        vy = minvecy
        oldpoint = minpoint
        B.append(minpoint)
    return B

T = int(input())
for test_case in range(T):
    N = int(input())
    X = []
    Y = []
    for i in range(N):
        xi,yi = [int(x) for x in input().split()]
        X.append(xi)
        Y.append(yi)
    print('Case #'+str(test_case+1)+':')
    B = boundary(X,Y)
    for i in range(N):
        if i in B:
            print(0)
        else:
            min_cut = 0
            for cut in B:
                tx = [X[a] for a in range(N) if a != cut]
                ty = [Y[a] for a in range(N) if a != cut]
                b1 = boundary(tx,ty)
                if any([X[i]==tx[k] and Y[i]==ty[k] for k in b1]):
                    min_cut = 1
                    break
                for cut in b1:
                    tx = [X[a] for a in range(N) if a != cut]
                    ty = [Y[a] for a in range(N) if a != cut]
                    b2 = boundary(tx,ty)
                    if any([X[i]==tx[k] and Y[i]==ty[k] for k in b2]):
                        min_cut = 2
                        break
                    for cut in b2:
                        tx = [X[a] for a in range(N) if a != cut]
                        ty = [Y[a] for a in range(N) if a != cut]
                        b3 = boundary(tx,ty)
                        if any([X[i]==tx[k] and Y[i]==ty[k] for k in b3]):
                            min_cut = 3
                            break
                        for cut in b3:
                            tx = [X[a] for a in range(N) if a != cut]
                            ty = [Y[a] for a in range(N) if a != cut]
                            b4 = boundary(tx,ty)
                            if any([X[i]==tx[k] and Y[i]==ty[k] for k in b4]):
                                min_cut = 4
                                break
                            if min_cut>0:
                                break
                        if min_cut>0:
                            break

                    if min_cut>0:
                        break
                if min_cut>0:
                    break
            print(min_cut)

