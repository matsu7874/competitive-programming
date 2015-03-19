MOD = 10**9+7
N = int(input())
A = [int(x) for x in input().split()]
B = [0 for _ in range(100)]
for a in A:
    B[a-1] += 1
ans = 0
for i in range(98):
    for j in range(i+1,99):
        for k in range(j+1,100):
            ans += B[i]*B[j]*B[k]

print(ans % MOD)