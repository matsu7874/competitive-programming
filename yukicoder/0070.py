N = int(input())
total = 0
for i in range(N):
    S, T = input().split()
    hs, ms = map(int, S.split(':'))
    ht, mt = map(int, T.split(':'))
    if hs < ht or (hs == ht and ms < mt):
        total += (ht - hs) * 60 + (mt - ms)
    else:
        total += (ht + 24 - hs) * 60 + (mt - ms)
print(total)
