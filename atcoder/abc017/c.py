(n, m) = [int(x) for x in input().split()]
if n>5001 or m>5001:
    exit()
M = [0 for i in range(m)]
L = []
R = []
S = []
SCORE = 0
for i in range(n):
    (l, r, s) = [int(x) for x in input().split()]
    for j in range(l,r+1):
        M[j-1] += 1
    SCORE += s
    L.append(l)
    R.append(r)
    S.append(s)
max_score = 0
for i in range(n):
    if 0 in M or 1 in M[L[i]-1:R[i]+1]:
        score = SCORE - S[i]
        max_score = max(max_score, score)
print(max_score)
