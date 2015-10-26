def each_digits(n, base=10):
    # 各桁の数字を得る
    digits = []
    a = 1
    while n >= a:
        digits.append(n // a % base)
        a *= base
    return digits[::-1]

N = int(input())
n = each_digits(N)
l = len(n)
for i in range(l - 1):
    ma = max(n[i + 1:])
    if ma <= n[i]:
        continue
    for j in range(l - 1, i, -1):
        if n[j] == ma:
            n[i], n[j] = n[j], n[i]
            answer = 0
            for a in n:
                answer *= 10
                answer += a
            print(answer)
            exit()
print(N)
