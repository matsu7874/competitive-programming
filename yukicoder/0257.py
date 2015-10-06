import sys
N, K = map(int, input().split())
d = (N-1)%(K+1)

while True:
    print(d)
    sys.stdout.flush()
    d += K+1
    n = int(input())
    if n >= N:
        exit()
