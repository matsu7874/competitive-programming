N = int(input())
T = [int(input()) for i in range(N)]
T.sort()
m = [0, 0]

elapsed_time = 0
while T:
    if m[0] == 0:
        m[0] = T.pop()
    elif m[1] == 0:
        m[1] = T.pop()
    t = min(m)
    for i in range(2):
        m[i] -= t
    elapsed_time += t
elapsed_time += max(m)
print(elapsed_time)
