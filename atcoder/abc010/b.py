n = int(input())
a = map(int, input().split())
cnt = 0
for b in a:
    while b % 2 == 0 or b % 3 == 2:
        b -= 1
        cnt += 1
print(cnt)
