import random
V = 50
edges = []
for i in range(V):
    for j in range(V):
        if i == j:
            continue
        edges.append((i, j, random.randint(1,10000000)))

# for i in range(V-1):
#     edges.append((i,i+1,1))

print(V, len(edges))
for e in edges:
    print(*e)
