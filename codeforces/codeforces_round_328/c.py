def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

t, w, b = map(int, input().split())
