n, m = map(int, input().split())
n %= 12
a = (360 * (n * 60 + m) / 720 - 360 * m / 60 + 360) % 360
print(min(360 - a, a))
