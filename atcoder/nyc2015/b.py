N = int(input())
A = []
for i in range(N):
    A.append(int(input()))
A.sort()
cnt = 0
w = 0
for a in A:
    if a>w:
        cnt += 1
        w += a
print(cnt)