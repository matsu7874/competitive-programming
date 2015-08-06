def area(r):
    return r*r*3.141592653589
N = int(input())
R = []
for i in range(N):
    R.append(int(input()))
R = sorted(R)[::-1]
d = 1
S = 0
for i in range(N):
    S += d*area(R[i])
    d *= -1
print(S)
