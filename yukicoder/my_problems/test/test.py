def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a


N = int(input())
A = [int(input()) for i in range(N)]

unit = A[0]
for i in range(1, N):
    unit = gcd(unit, A[i])

print(100 // unit)
