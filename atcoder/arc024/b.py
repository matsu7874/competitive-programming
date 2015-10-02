N = int(input())
color = [int(input()) for i in range(N)]
color = color * 2
max_length = 0
length = 0
for i in range(1, N * 2):
    if color[i - 1] == color[i]:
        length += 1
    else:
        max_length = max(max_length, length)
        length = 0
max_length = max(max_length, length)
if max_length >= N:
    print(-1)
else:
    print((max_length // 2 + 1))
