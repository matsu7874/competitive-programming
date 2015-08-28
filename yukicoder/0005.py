L = int(input())
N = int(input())
W = [int(x) for x in input().split()]
W.sort()
w = 0
cnt = 0
for i in range(N):
    if w + W[i] > L:
        print(i)
        exit()
    else:
        w += W[i]
print(N)
