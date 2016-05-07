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
    a = [[2, -1, -4], [-2, -1, -2]]
    print(*a, sep='\n')

    state, a = gauss_jordan_elimination(a)
    print('row reduce')
    print(state)
    print(*a, sep='\n')
