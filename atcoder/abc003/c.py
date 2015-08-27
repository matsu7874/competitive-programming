(N, K) = [int(x) for x in input().split()]
R = [int(x) for x in input().split()]
R.sort()
rate = 0
for i in range(N - K, N):
    rate = (rate + R[i]) / 2
print(rate)
