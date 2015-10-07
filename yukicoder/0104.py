S = input()

if S == '':
    print(1)
    exit()

size = len(S)
cur = 2**size
for i in range(size):
    if S[i] == 'R':
        cur += 2**(size - 1 - i)
print(cur)
