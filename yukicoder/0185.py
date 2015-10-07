N = int(input())
x, y = map(int, input().split())
ans = y - x
for i in range(N - 1):
    x, y = map(int, input().split())
    if y - x != ans:
        print(-1)
        exit()
if ans > 0:
    print(ans)
else:
    print(-1)
