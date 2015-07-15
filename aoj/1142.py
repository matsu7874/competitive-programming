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
    p_list.add(2)
    return p_list

def main():
    m = int(input())
    for _ in range(m):
        s = input()
        S = set()
        l = len(s)
        for i in range(1, l):
            S.add(s[0:i]+s[i:l])
            S.add(s[0:i][::-1]+s[i:l])
            S.add(s[0:i]+s[i:l][::-1])
            S.add(s[0:i][::-1]+s[i:l][::-1])
            S.add(s[i:l]+s[0:i])
            S.add(s[i:l][::-1]+s[0:i])
            S.add(s[i:l]+s[0:i][::-1])
            S.add(s[i:l][::-1]+s[0:i][::-1])
        print(len(S))
        # print(S)



if __name__ == '__main__':
    main()
