N = int(input())
X = [int(x) for x in input().split()]
X = list(set(X))
X.sort()
N = len(X)
if N == 1:
    print(0)
    exit()
print(min([X[i+1]-X[i] for i in range(N-1)]))