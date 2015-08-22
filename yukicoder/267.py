N = int(input())
A = input().split()
B = []
C = ['D', 'C', 'H', 'S']
for i in range(N):
    if A[i][1] in 'ATJQK':
        B.append((C.index(A[i][0]), [1,10,11,12,13]['ATJQK'.index(A[i][1])]))
    else:
        B.append((C.index(A[i][0]), int(A[i][1])))
B.sort()
ans = ''
for b in B:
    if b[1] in [1,10,11,12,13]:
        ans += C[b[0]] + 'ATJQK'[[1,10,11,12,13].index(b[1])] + ' '
    else:
        ans += C[b[0]] + str(b[1]) + ' '
print(ans[:-1])
