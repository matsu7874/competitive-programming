N,M,K = map(int, input().split())
graph = [[[],[]] for i in range(N)]
for i in range(M):
    a,b,c = map(int, input().split())
    graph[a-1][0].append(b-1)
    graph[a-1][1].append(c)
    graph[b-1][0].append(a-1)
    graph[b-1][1].append(c)
d = list(map(int, input().split()))
candidate = [True for i in range(N)]
for i in range(K):
    next_candidate = [False for i in range(N)]
    for j in range(N):
        if not candidate[j]:
            continue
        for k in range(len(graph[j][0])):
            nv = graph[j][0][k]
            cost = graph[j][1][k]
            if cost == d[i]:
                next_candidate[nv] = True
    candidate = next_candidate[:]
ans = []
for i in range(N):
    if candidate[i]:
        ans.append(i+1)
ans.sort()
print(len(ans))
print(*ans)
