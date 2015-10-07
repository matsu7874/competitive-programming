N = int(input())
X = list(map(int, input().split()))
cnt = 0
for x in X:
    if x % 2 == 0:
        cnt += 1
    else:
        cnt -= 1
print(abs(cnt))
