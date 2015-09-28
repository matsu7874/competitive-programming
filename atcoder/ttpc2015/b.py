N, B, C = map(int, input().split())
A = list(map(int, input().split()))
A.reverse()
total = 0
happiness = 0
day = 0
while day < N and total < C:
    happiness += A[day] * min(B, max(0, C - total))
    total += min(B, max(0, C - total))
    day += 1
print(happiness)
