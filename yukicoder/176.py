S = input()
n = 0
for i in range(len(S)):
    n += 2 ** i
    if S[i] == 'L':
        n += 1
    if S[i] == 'R':
        n += 2
print(n)