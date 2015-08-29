N = int(input())
A = set()
cnt = 0
for i in range(N):
    a = int(input())
    if a in A:
        cnt += 1
    else:
        A.add(a)
print(cnt)
