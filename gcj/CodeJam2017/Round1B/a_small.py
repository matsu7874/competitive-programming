def solve(d, n, hs):
    max_t = 0
    for i in range(n):
        k, s = hs[i]
        max_t = max(max_t, (d-k)/s)
    return d/max_t

def print_answer(t, ans):
    tmpl = 'Case #{0}: {1}'
    print(tmpl.format(t+1, ans))

if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        D, N = map(int, input().split())
        H = [map(int, input().split()) for i in range(N)]
        ans = solve(D, N, H )
        print_answer(_, ans)
