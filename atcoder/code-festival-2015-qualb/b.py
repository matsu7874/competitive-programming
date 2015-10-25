N, M = map(int, input().split())
A = list(map(int, input().split()))
cnt = [0 for i in range(M + 1)]
for a in A:
    cnt[a] += 1
for i in range(M + 1):
    if cnt[i] > N // 2:
        print(i)
        exit()
print('?')
