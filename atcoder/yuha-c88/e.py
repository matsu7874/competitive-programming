def main():
    n = int(input())
    S = [input() for i in range(n)]
    M = [input() for i in range(5)]

    w = [M[0][2], M[2][0], M[2][4], M[4][2]]
    S = [s for s in S if (s[0] in w or s[1] in w)]
    
    ans = []
    if M[1][2] == '↓':
        for s in S:
            if s[0] == M[0][2]:
                ans.append(s[1])
    else:
        for s in S:
            if s[1] == M[0][2]:
                ans.append(s[0])
    S = [s for s in S if s[0] in ans or s[1] in ans]
    ans = []
    if M[2][1] == '→':
        for s in S:
            if s[0] == M[2][0]:
                ans.append(s[1])
    else:
        for s in S:
            if s[1] == M[2][0]:
                ans.append(s[0])
    S = [s for s in S if s[0] in ans or s[1] in ans]
    ans = []
    if M[2][3] == '←':
        for s in S:
            if s[0] == M[2][4]:
                ans.append(s[1])
    else:
        for s in S:
            if s[1] == M[2][4]:
                ans.append(s[0])
    S = [s for s in S if s[0] in ans or s[1] in ans]
    ans = []
    if M[3][2] == '↑':
        for s in S:
            if s[0] == M[4][2]:
                ans.append(s[1])
    else:
        for s in S:
            if s[1] == M[4][2]:
                ans.append(s[0])
    S = [s for s in S if s[0] in ans or s[1] in ans]

    if M[1][2] == '↓':
        for s in S:
            if s[0] == M[0][2]:
                print(s[1])
                return
    else:
        for s in S:
            if s[1] == M[0][2]:
                print(s[0])
                return


if __name__ == '__main__':
    main()
