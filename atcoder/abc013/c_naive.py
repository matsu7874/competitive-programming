N, H = map(int, input().split())
A, B, C, D, E = map(int, input().split())


def can_alive(hungry, money):
    for normal in range((money + A - 1) // A + 1):
        simple = max(0, (money - (A * normal)) // C)
        fast = (hungry + (normal * B) + (simple * D)) // E
        alive_day = normal + simple + fast
        if alive_day >= N:
            print(money, normal, simple, fast, alive_day)
            return True
    return False


def solve(n, h):
    l = 0
    r = n * C
    while l + 1 < r:
        m = (l + r) // 2
        flag = can_alive(H, m)
        if flag:
            r = m
        else:
            l = m
    return r

if __name__ == '__main__':
    print(N,H)
    print(A, B, C, D, E)
    print(solve(N, H))
    print('YEN de OK')
