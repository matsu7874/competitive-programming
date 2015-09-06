N = int(input())
total = 0
total += 100 * (N // 10)
if N % 10 > 6:
    total += 100
else:
    total += 15 * (N % 10)
print(total)
