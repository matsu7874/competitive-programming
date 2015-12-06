A=[20104,20063,19892,20010,19874,20199,19898,20163,19956,19841]
S=input()
if S[0] != '3':
    print(S[0],3)
    exit()
for c in S[2:]:
    A[int(c)] -= 1
print(A.index(-1), A.index(1))
