S = input()
T = input()
ATCODER = 'atcoder'
l = len(S)
for i in range(l):
    if S[i] != T[i]:
        if S[i] != '@' and T[i] != '@':
            print('You will lose')
            exit()
        elif S[i] == '@' and T[i] not in ATCODER:
            print('You will lose')
            exit()
        elif T[i] == '@' and S[i] not in ATCODER:
            print('You will lose')
            exit()
print('You can win')
