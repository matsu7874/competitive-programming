n = int(input())
a = list(set([int(input()) for x in range(n)]))
a.sort()
print(a[-2])
