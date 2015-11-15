def bibun(n,c):
    if n<c:
        return 0
    res = 1
    for i in range(c):
        res *= n
        n -= 1
    return res

def main():
    N = int(input())
    d = int(input())
    S = input()
    A = [0 for i in range(d+1)]
    d_cnt = 0
    x_cnt = 0
    a = 0
    pre = ''
    for s in S:
        if s in '123456789':
            if a==0:
                a = int(s)
            else:
                a *= int(s)
        elif s == '{':
            d_cnt += 1
        elif s == '}':
            if x_cnt >= d_cnt:
                A[x_cnt-d_cnt] += a*bibun(x_cnt, d_cnt)
            x_cnt = 0
            a = 0
            d_cnt -= 1
        elif s == '+':
            if x_cnt >= d_cnt:
                A[x_cnt-d_cnt] += a*bibun(x_cnt, d_cnt)
            x_cnt = 0
            a = 0
        elif s == 'x':
            x_cnt += 1
            if a == 0:
                a = 1
    if x_cnt >= d_cnt:
        A[x_cnt - d_cnt] += a * bibun(x_cnt, d_cnt)
    ans = ''
    for ai in A:
        ans += str(ai) + ' '
    print(ans[:-1])





if __name__ == '__main__':
    main()
