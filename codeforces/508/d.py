N = int(input())
passwords = ['' for i in range(N)]
for i in range(N):
    passwords[i] = input()

path = [[] for i in range(N)]
for i in range(N):
    for j in range(N):
        if i != j and passwords[i][1:] == passwords[j][0:2]:
            path[i].append(j)
i = 0
flg = True
while flg:
    flg = False
    i = 0
    while i<N:
        if len(path[i]) == 1:
            flg = True
            t = path[i][0]
            passwords[i] = passwords[i][0:-2] + passwords[t]
            path[i] = path[t]
            if i in path[i]:
                path[i].remove(i)
            passwords[t] = ''
            path[t] = []
            for j in range(N):
                if t in path[j]:
                    path[j].remove(t)
                    if i not in path[j]:
                        path[j].append(i)
        print(path)
        i += 1

    if all([len(x)>1 for x in path if len(x)>1]):
        path[min([x for x in path[]])].pop(0)
        flg = True
for p in passwords:
    if len(p) == N+2:
        print('YES')
        print(p)
        exit()
print('NO')