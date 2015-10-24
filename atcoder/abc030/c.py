N, M = map(int, input().split())
X, Y = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

cnt = 0
time = 0
pos = 0

pre_a = -1
pre_b = -1

while (time <= A[-1] and pos == 0) or (time <= B[-1] and pos == 1):
    if pos == 0:
        l = pre_a + 1
        r = N
        first = None
        while l <= r:
            m = (l + r) // 2
            if A[m] >= time:
                first = m
                r = m - 1
            else:
                l = m + 1
        if first is None:
            break
        pre_a = first
        pos = 1
        time = A[first] + X
    else:
        l = pre_b + 1
        r = M
        first = None
        while l <= r:
            m = (l + r) // 2
            if B[m] >= time:
                first = m
                r = m - 1
            else:
                l = m + 1
        if first is None:
            break
        pre_b = first
        pos = 0
        cnt += 1
        time = B[first] + Y
print(cnt)
