def cal(n,k,p):
    dp = [[0 for j in range(n+1)] for i in range(n+1)]
    dp[0][0] = 1
    for i in range(1, n+1):
        for j in range(i+1):
            dp[i][j] = dp[i-1][j] * (1 - p[i-1])
            if j > 0:
                dp[i][j] += dp[i-1][j-1] * p[i-1]
    return sum(dp[n][k:])
                

def solve(n, k, u, p):
    p.sort()
    p.append(1)
    _p = p[:]
    _u = u
    maxp = 0
    # print(p)
    # top_tを強化
    for t in range(k+1):
        p = _p[:]
        u = _u
        print('TOP ',t)
        print(p)
        for i in range(n-t, n):
            if p[i] < p[i+1]:
                pp = min(u/(i+1-n+t), p[i+1]-p[i])
                # print(t,i,n-t, i+1)
                for j in range(n-t, i+1):
                    p[j] += pp
                    u -= pp
            print(p)
        print('Bottom')
        for i in range(n):
            if p[i] < p[i+1]:
                pp = min(u/(i+1), p[i+1]-p[i])
                for j in range(i+1):
                    p[j] += pp
                    u -= pp
                print(p)
        # ret = 1
        # for i in range(n):
        #     ret *= p[i]
        # print(p)
        
        maxp = max(maxp, cal(n,k,p))
    # print(p)
    return maxp


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
