N = int(input())
cur = 0
cnt = 0
while 10**cur < N:
    cnt += (N + 1) // (10**(cur + 1)) * (10**cur)
    cnt += max(min((N + 1) % (10**(cur + 1)) - (10**cur), 10**cur), 0)
    cur += 1
if 10**cur == N:
    cnt += 1
print(cnt)
