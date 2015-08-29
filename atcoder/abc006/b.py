n = int(input())
a = [0 for i in range(n + 3)]
a[3] = 1
for i in range(4, n + 1):
    a[i] = (a[i - 1] + a[i - 2] + a[i - 3]) % 10007
print(a[n])
