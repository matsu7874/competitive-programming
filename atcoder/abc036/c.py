n = int(input())
a = [int(input()) for i in range(n)]
b = list(set(a))
b.sort()
for i in range(n):
    print(b.index(a[i]))
