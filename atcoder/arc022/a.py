S=input()
flags=[False]*3
for c in S:
    if c in 'iI':
        flags[0] = True
    elif c in 'cC' and flags[0]:
        flags[1] = True
    elif c in 'tT' and flags[1]:
        print('YES')
        exit()
print('NO')
