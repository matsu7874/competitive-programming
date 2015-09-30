N = int(input())
m = list(map(int, input().split()))
print(sum(max(80 - m[i], 0) for i in range(N)))
