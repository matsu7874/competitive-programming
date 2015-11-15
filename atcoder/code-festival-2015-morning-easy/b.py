N =int(input())
S = input()
if N%2==1:
    print(-1)
    exit()
t = len(S) // 2
cnt = 0
for i in range(t):
    if S[i] != S[i + t]:
        cnt += 1
print(cnt)
