N = int(input())
B = [0, 0]
for i in range(N-1):
    B.append(int(input()))
S = []
for i in range(0, N+1):
    s = []
    for j in range(i+1, N+1):
        if B[j] == i:
            s.append(j)
    S.append(s)

fee = [0 for i in range(N+1)]
for i in range(1,N+1)[::-1]:
    if(len(S[i]) == 0):
        fee[i] = 1
    elif(len(S[i]) < 3):
        fee[i] = fee[S[i][0]] + fee[S[i][-1]] + 1
    else:
        max_fee = 0
        min_fee = 99999999
        for j in range(len(S[i])):
            max_fee = max(max_fee, fee[S[i][j]])
            min_fee = min(min_fee, fee[S[i][j]])
        fee[i] = max_fee + min_fee + 1
print(fee[1])
