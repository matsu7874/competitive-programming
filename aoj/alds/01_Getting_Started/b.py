def gcd(a, b):
    # 最大公約数
    while b > 0:
        a, b = b, a % b
    return a
a, b = map(int, input().split())
print(gcd(a, b))
