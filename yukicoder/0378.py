n = int(input())
a = [n]
while a[-1] > 0:
    a.append(a[-1] // 2)
normal = sum(a)
print(a[0] * 2 - sum(a))
