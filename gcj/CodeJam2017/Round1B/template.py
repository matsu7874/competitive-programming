def solve(r, c, cake):

    return ret

def print_answer(t, ans):
    tmpl = 'Case #{0}: {1}'
    print(tmpl.format(t+1, ans))

if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        R,C = map(int, input().split())
        cake = [[x for x in input()] for i in range(R)]
        ans = solve(R,C,cake)
        print_answer(_, ans)