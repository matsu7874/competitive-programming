def find(union_find_parent, x):
    if union_find_parent[x] != x:
        union_find_parent[x] = find(union_find_parent, union_find_parent[x])
    return union_find_parent[x]

def union(union_find_parent, x, y):
    union_find_parent[find(union_find_parent, x)] = find(union_find_parent, y)

if __name__ == '__main__':
    N, Q = [int(x) for x in input().split()]
    union_find_parent = [i for i in range(N)]
    for _ in range(Q):
        P, A, B = [int(x) for x in input().split()]
        if P == 0:
            union(union_find_parent, A, B)
        if P == 1:
            if find(union_find_parent, A) == find(union_find_parent, B):
                print('Yes')
            else:
                print('No')
