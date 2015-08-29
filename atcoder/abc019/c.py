N = int(input())
A = [int(i) for i in input().split()]
A.sort()
B = set()
for i in range(N):
    while A[i] % 2 == 0:
        A[i] //= 2
    B.add(A[i])
print(len(B))
