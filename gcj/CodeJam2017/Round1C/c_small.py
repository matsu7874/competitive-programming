def solve(n, k, u, p):
    p.sort()
    p.append(1)
    # print(p)
    for i in range(n):
        if p[i] < p[i+1]:
            pp = min(u/(i+1), p[i+1]-p[i])
            for j in range(i+1):
                p[j] += pp
                u -= pp
            # print(p)
    ret = 1
    for i in range(n):
        ret *= p[i]
    # print(p)
    return ret

def print_answer(t, ans):
    tmpl = 'Case #{0}: {1}'
    print(tmpl.format(t+1, ans))

if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        N,K = map(int, input().split())
        U = float(input())
        P = list(map(float, input().split()))
        
        ans = solve(N, K, U, P)
        print_answer(_, ans)
