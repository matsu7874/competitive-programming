N = int(input())
A = list(map(int, input().split()))

crane = 0
tortoise = 0
for i in range(N):
    crane += 2 * (N - 1) - A[i] // 2
    tortoise += A[i] // 2 - (N - 1)

crane //= (N - 1)
tortoise //= (N - 1)
print(crane, tortoise)
