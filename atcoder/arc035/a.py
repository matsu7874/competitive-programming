S=input()
l = len(S)
for i in range(l//2+1):
    if S[i]=='*' or S[l-1-i]=='*' or S[i]==S[l-1-i]:
        pass
    else:
        print('NO')
        exit()
print('YES')
