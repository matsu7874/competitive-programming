tetrahedrals = [n * (n + 1) * (n + 2) // 6 for n in range(0, 182)]
odd_tetrahedrals = [tetrahedrals[i] for i in range(182) if tetrahedrals[i] % 2 == 1]
N = 10**6
dp_all = [N] * (N+1)
dp_odd = [N] * (N+1)

for t in tetrahedrals:
    if N<=t:
        print(t)
        break
    dp_all[t]=1
for i in range(N):
    for t in tetrahedrals:
        if N <= i + t:
            break
        dp_all[i + t] = min(dp_all[i + t], dp_all[i] + 1)

for t in odd_tetrahedrals:
    if N<=t:
        print(t)
        break
    dp_odd[t] = 1
for i in range(N):
    for t in odd_tetrahedrals:
        if N <= i + t:
            break
        dp_odd[i + t] = min(dp_odd[i + t], dp_odd[i] + 1)
while True:
    n = int(input())
    if n == 0:
        break
    print(dp_all[n], dp_odd[n])
