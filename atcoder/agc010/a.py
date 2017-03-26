n = int(input())
a = list(map(int, input().split()))
cnt = [0, 0]
for v in a:
    cnt[v%2] += 1
if (cnt[1]%2 == 0) or (cnt[1]%2 == 1 and cnt[0] == 0):
    print('YES')
else:
    print('NO')
    