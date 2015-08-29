N = int(input())
D = [int(input()) for i in range(N)]
D.sort()
max_length = sum(D)
max_edge = max(D)
if max_edge * 2 > max_length:
    min_length = 2 * max_edge - max_length
else:
    min_length = 0

print(max_length)
print(min_length)
