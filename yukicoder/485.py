N = int(input())
A = [int(x) for x in input().split()]
cnt = 0
for a in A:
    if A.count(a) == 1:
        cnt += 1
print(cnt)