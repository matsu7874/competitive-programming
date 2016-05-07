def intersection(a1, b1, c1, a2, b2, c2):
    # find the point of lines intersection. a1x+b1y+c1=0 and a2x+b2y+c2=0.
    # if these lines do not have intersection, return (inf,inf)
    d = a1 * b2 - a2 * b1
    if d == 0:
        return (float('inf'), float('inf'))
    if a1 == 0:
        x = (b2*c1-b1*c2)/(a2*b1)
        y = -c1/b1
        return (x,y)
    else:
        y =-(a1*c2-a2*c1)/(a1*b2-b1*a2)
        x = -(b1*y+c1)/a1
        return (x,y)

def gauss_jordan_elimination(Array):
    # N行M列のArray
    N = len(Array)
    if N == 0:
        return (True, Array)
    else:
        M = len(Array[0])

    A = []
    for i in range(len(Array)):
        A.append(Array[i][:])

    pivot = 0
    L = min(N, M)
    while pivot < L:
        pivot_v = A[pivot][pivot]
        pivot_row = pivot
        for i in range(pivot + 1, L):
            v = max(A[i][pivot], -A[i][pivot])
            if pivot_v < v:
                pivot_row = i
                pivot_v = v
        if pivot_row > pivot:
            for i in range(M):
                A[pivot][i], A[pivot_row][i] = A[pivot_row][i], A[pivot][i]
        if pivot_v == 0:
            return ('False', A)
        inv_pivot = 1 / A[pivot][pivot]
        A[pivot][pivot] = 1
        for i in range(pivot+1, M):
            A[pivot][i] *= inv_pivot
        for i in range(N):
            if i == pivot:
                continue
            t = -1 * A[i][pivot]
            A[i][pivot] = 0
            for j in range(pivot+1,M):
                A[i][j] += t * A[pivot][j]
        pivot += 1

    return (True, A)

if __name__ == '__main__':
    import random
    for i in range(10000):
        a,b,c,d,e,f = [random.randint(-1000,1000) for i in range(6)]
        print(a,b,c,d,e,f,end=' ')
        array=[[a,b,-c],[d,e,-f]]

        state, array = gauss_jordan_elimination(array)

        x,y = intersection(a,b,c,d,e,f)

        if abs(array[0][2]- x)<0.00001 and abs(array[1][2] - y)<0.00001:
            print('OK')
        else:
            print((array[0][2],array[1][2]),(x,y))
            exit()
