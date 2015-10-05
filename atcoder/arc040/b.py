N, R = map(int, input().split())
S = [c for c in input()]
last_space = N - 1
while last_space >= 0:
    if S[last_space] == '.':
        break
    last_space -= 1
i = 0
time = 0
while i < last_space - R + 1:
    time += 1
    if S[i] == '.':
        for j in range(R):
            S[i + j] = 'o'
    else:
        i += 1
else:
    if last_space>=0:
        time += 1
        for j in range(R):
            S[i + j] = 'o'
print(time)
