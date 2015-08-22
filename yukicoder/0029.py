N = int(input())
item = [0 for i in range(10)]
for i in range(N):
    a,b,c = [int(x)-1 for x in input().split()]
    item[a] += 1
    item[b] += 1
    item[c] += 1
cnt = 0
for i in range(10):
    cnt += item[i]//2
    item[i] %= 2
cnt += sum(item)//4
print(cnt)
