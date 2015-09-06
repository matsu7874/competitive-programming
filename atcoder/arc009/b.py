def each_digits(n, base=10):
    digits = []
    a = 1
    while n >= a:
        digits.append(n // a % base)
        a *= base
    return digits[::-1]


def convert(A, B):
    res = []
    for a in A:
        res.append(B.index(a))
    if len(res) == 1:
        return res[0]
    else:
        return int(''.join(str(res[i]) for i in range(len(res))))

B = list(map(int, input().split()))
N = int(input())
A = [int(input()) for i in range(N)]
C = [(convert(each_digits(A[i]), B), A[i]) for i in range(N)]
C.sort()
for i in range(N):
    print(C[i][1])
