N,K=map(int, input().split())
X=list(map(int, input().split()))
cur = K-1
win_value = min(X[:cur])
if X[0]>X[1]:
    winner = 1
print(winner+1)
