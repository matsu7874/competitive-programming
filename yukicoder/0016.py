x, N = map(int, input().split())
A = list(map(int, input().split()))
if x == 0 or x == 1:
    print(x * N)
    exit()

power = [x]
i = 0
while 2**i < 100000000:
    power.append(power[i] * power[i] % 1000003)
    i += 1
bit_max = i

P = []
for i in range(N):
    a = 1
    for j in range(bit_max + 1):
        if A[i] & (2**j):
            a *= power[j]
    P.append(a)
print(sum(P) % 1000003)
