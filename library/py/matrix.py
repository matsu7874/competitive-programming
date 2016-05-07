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
    a,b = matrix2_power([[1,1],[1,0]],int(input()))
    print(sum(a))
