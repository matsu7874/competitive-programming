def dicide_tower(n, move, it):
    if (n+it)%2 == 0:
        return [0,2,1][move%3]
    else:
        return [0,1,2][move%3]

def solve(n, t):
    move = [0 for _ in range(n)]
    T = [[] for _ in range(3)]
    for i in range(n):
        move[i] = t//(2**i) - t//(2**(i+1))
    for i in range(n,0,-1):
        T[dicide_tower(n,move[i-1],i)].append(i)
    for t in T:
        if len(t) == 0:
            print('-')
        else:
            buff = ''
            for c in map(str,t):
                buff += ' '+c
            print(buff[1:])

def main():
    (n, t) = [int(x) for x in input().split()]
    solve(n,t)

if __name__ == '__main__':
    main()