S = input()
ans = set()
for i in range(2**len(S)):
    S2 = S[:]
    T = ''
    front = 0
    back = len(S) - 1
    for j in range(len(S)):
        if i & (2 << j):
            T += S[front]
            front += 1
        else:
            T += S[back]
            back -= 1
    ans.add(T[:])
print(len(ans))
