class Matrix():

    def __init__(self, array):
        self.r = len(array)
        self.c = len(array[0])
        self.matrix = []
        for i in range(self.r):
            self.matrix.append(array[i][:])

    def component(self, i, j):
        return self.matrix[i][j]

    def row(self, n):
        return self.matrix[n]

    def column(self, n):
        return [self.matrix[i][n] for i in range(self.r)]

    def transpose(self):
        return Matrix(list(map(list, zip(*self.matrix))))

    def display(self):
        for i in range(self.r):
            print(self.matrix[i])

    def copy(self):
        return Matrix([[self.matrix[i][j] for j in range(self.c)] for i in range(self.r)])

    def add(self, a):
        b = self.copy()
        for i in range(self.r):
            for j in range(self.c):
                b.matrix[i][j] += a.matrix[i][j]
        return b

    def subtract(self, a):
        b = self.copy()
        for i in range(self.r):
            for j in range(self.c):
                b.matrix[i][j] -= a.matrix[i][j]
        return b

    def times(self, real):
        a = self.copy()
        for i in range(self.r):
            for j in range(self.c):
                a.matrix[i][j] *= real
        return a

    def dot_product(self, a):
        b = [[] for i in range(self.r)]
        for i in range(self.r):
            for j in range(a.c):
                t = 0
                for k in range(self.c):
                    t += self.matrix[i][k] * a.matrix[k][j]
                b[i].append(t)
        return Matrix(b)

    def rank(self, a):
        # O(n m^2)
        n = len(a)
        m = len(a[0])

        return 0

    def determinant_naive(self):
        # require regular matrix
        if self.r == 1:
            return self.matrix[0][0]
        elif self.r == 2:
            return self.matrix[0][0] * self.matrix[1][1] - self.matrix[1][0] * self.matrix[0][1]
        det = 0
        for i in range(n):
            if self.matrix[i][0] == 0:
                continue
            cofactor = []
            for j in range(0, n):
                if i == j:
                    continue
                cofactor.append(self.matrix[j][1:])
            sign = -1 if (i + j) % 2 else 1
            cofactor = Matrix(cofactor)
            det += sign * self.matrix[i][0] * cofactor.determinant_naive()
        return det

    def LU_decomposition(self):
        n = self.r
        L = Matrix([[0 for j in range(n)] for i in range(n)])
        U = Matrix([[0 for j in range(n)] for i in range(n)])
        for i in range(n):
            L.matrix[i][i] = 1
        for k in range(n):
            U.matrix[k][k] = self.matrix[k][k]
            for i in range(k+1, n):
                L.matrix[i][k] = self.matrix[i][k] / U.matrix[k][k]
                U.matrix[k][i] = self.matrix[k][i]
            for i in range(k+1, n):
                for j in range(k+1,n):
                    self.matrix[i][j] -= L.matrix[i][k] * U.matrix[k][j]
        return L,U


    def gauss_jordan_elimination(self):
        a = self.copy()
        pivot = 0
        L = min(self.r, self.c)
        while pivot < L:
            pivot_v = a.matrix[pivot][pivot]
            pivot_row = pivot
            for i in range(pivot + 1, L):
                v = max(a.matrix[i][pivot], -a.matrix[i][pivot])
                if pivot_v < v:
                    pivot_row = i
                    pivot_v = v
            if pivot_row > pivot:
                for i in range(self.c):
                    a.matrix[pivot][i], a.matrix[pivot_row][i] = a.matrix[pivot_row][i], a.matrix[pivot][i]
            if pivot_v == 0:
                pivot += 1
                continue
            inv_pivot = 1 / a.matrix[pivot][pivot]
            a.matrix[pivot][pivot] = 1
            for i in range(pivot+1, self.c):
                a.matrix[pivot][i] *= inv_pivot
            for i in range(self.r):
                if i == pivot:
                    continue
                t = -1 * a.matrix[i][pivot]
                a.matrix[i][pivot] = 0
                for j in range(pivot+1,self.c):
                    a.matrix[i][j] += t * a.matrix[pivot][j]
            pivot += 1

        return (a)


def matrix2_product(a, b):
    p1 = (a[0][0] + a[1][1]) * (b[0][0] + b[1][1])
    p2 = (a[1][0] + a[1][1]) * b[0][0]
    p3 = a[0][0] * (b[0][1] - b[1][1])
    p4 = a[1][1] * (b[1][0] - b[0][0])
    p5 = (a[0][0] + a[0][1]) * b[1][1]
    p6 = (a[1][0] - a[0][0]) * (b[0][0] + b[0][1])
    p7 = (a[0][1] - a[1][1]) * (b[1][0] + b[1][1])
    c = [[p1 + p4 - p5 + p7, p3 + p5], [p2 + p4, p1 + p3 - p2 + p6]]
    for i in range(2):
        for j in range(2):
            c[i][j] %= 1000000007
    return c


def matrix2_power(mtr, p):
    if p == 0:
        return [[1, 0], [0, 1]]
    x = [[1, 0], [0, 1]]
    x = matrix2_product(x, mtr)
    ans = [[1, 0], [0, 1]]
    while p > 0:
        if p % 2 == 0:
            x = matrix2_product(x, x)
            p //= 2
        else:
            ans = matrix2_product(ans, x)
            p -= 1
    return ans

if __name__ == '__main__':
    n = 3
    A = [[i * 100 + j for j in range(n)] for i in range(n)]
    B = [[i * 100  for j in range(n)] for i in range(n)]
    I = [[2 if i == j else 0 for j in range(n)] for i in range(n)]
    A = [[2,3,1,5],[6,13,5,19],[2,19,10,23],[4,10,11,31]]
    a = Matrix(A)
    b = Matrix(B)
    a.display()
    b.display()

    # a.dot_product(b).display()
    print(a.determinant_naive())

    # import time
    # START_TIME = time.time()
    # at = a.transpose()
    # ELAPSED_TIME = time.time() - START_TIME
    # print('elapsed time is:', ELAPSED_TIME, '[s]')
    l,u = a.LU_decomposition()
    l.display()
    u.display()
    a.gauss_jordan_elimination().display()
    b.gauss_jordan_elimination().display()
