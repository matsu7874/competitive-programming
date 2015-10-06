N = int(input())
total = 0
for i in range(N):
    S, T = input().split()
    H, M = map(int, S.split(':'))
    h, m = map(int, T.split(':'))
    if H<h:
        total += (h-H) * 60 + (m - M)
    else:
        total += (h+24-H) * 60 + (m - M)
print(total)
