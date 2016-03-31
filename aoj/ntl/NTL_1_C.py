def gcd(a, b):
    # 最大公約数
    while b > 0:
        a, b = b, a % b
    return a


def lcm(a, b):
    # 最小公倍数
    return a * b // gcd(a, b)

n = int(input())
a = list(map(int, input().split()))
ans = a[0]
for i in range(1,n):
    ans = lcm(ans, a[i])
print(ans)
