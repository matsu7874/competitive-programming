def solve(n,q,h,g,w):
    total = g[0][1]/h[0]
    total = [[float('inf') for j in range(n)] for i in range(n)]
    for i in range(n-1):
        for j in range(i+1, n):
            if 

    ch = h[0]
    ch[0] -= g[][1]
    for i in range(1, n-1):
        if g[i][i+1] < 
    return ret

def print_answer(t, ans):
    tmpl = 'Case #{0}: {1}'
    print(tmpl.format(t+1, ans))

if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        N,Q = map(int, input().split())
        H = []
        for i in range(N):
            e,s = map(int, input().split())
            H.append([e,s])
        G = []
        for i in range(N):
            G.append(list(map(int, input().split())))
        W = []
        for i in range(Q):
            u,v = map(int, input().split())
            W.append((u,v))

        ans = solve(N,Q, H, G,W)
        print_answer(_, ans)