def factrial(n):
    res = 1
    while n > 1:
        res *= n
        n -= 1
    return res

N = int(input())
T = [int(input()) for i in range(N)]
T.sort()

penalty = 0
d = dict()
for i in range(N):
    penalty += T[i] * (N - i)
    if T[i] in d:
        d[T[i]] += 1
    else:
        d.update({T[i]: 1})
print(penalty)

pattern = 1
for k, v in d.items():
    pattern = pattern * factrial(v) % 1000000007
print(pattern)
