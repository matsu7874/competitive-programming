n,l=map(int, input().split())
s=input()
cnt = 1
total = 0
for c in s:
    if c == '+':
        cnt += 1
        if cnt > l:
            cnt = 1
            total += 1
    else:
        cnt -= 1
print(total)
