n = int(input())
S = [input()[::-1] for i in range(n)]
S.sort()
for s in S:
    print(s[::-1])
