union_find_parent = {}

def find(x):
    if union_find_parent[x] != x:
        union_find_parent[x] = find(union_find_parent[x])
    return union_find_parent[x]

def union(x, y):
    union_find_parent[find(x)] = find(y)


(N, M) = [int(x) for x in input().split()]
for i in range(N):
    union_find_parent[i+1] = i+1

for _ in range(M):
    (a, b) = [int(x) for x in input().split()]
    union(a, b)

cnt = 0
for k, v in union_find_parent.items():
    if k == v:
        cnt += 1
print(cnt-1)