def prime_list(n):
    p = [True for i in range(n)]
    p[0] = False
    p[1] = False
    for j in range(4, n, 2):
            p[j] = False
    i = 3
    while i*i < n:
        if p[i]:
            for j in range(2*i, n, i):
                p[j] = False
        i += 2
    p_list = [2*i+1 for i in range(1,n//2) if p[2*i+1]]
    p_list.append(2)
    return p_list

def main():
    p_list = set(prime_list(1000000))

    while True:
        a,d,n = [int(x) for x in input().split()]
        if a == 0 and d == 0 and n == 0:
            exit()
        cnt = 0
        a -= d
        while cnt < n:
            a += d
            if a in p_list:
                cnt += 1
        print(a)

if __name__ == '__main__':
    main()
