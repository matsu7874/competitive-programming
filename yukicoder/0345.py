s = input()
n = len(s)
ans = float('inf')
for i in range(n - 2):
    if s[i] == 'c':
        w_cnt = 0
        for j in range(i + 1, n):
            if s[j] == 'w':
                if w_cnt == 1:
                    ans = min(ans, j - i + 1)
                    break
                else:
                    w_cnt += 1
if ans > n:
    ans = -1
print(ans)
