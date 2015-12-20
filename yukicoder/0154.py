T = int(input())
for i in range(T):
    possible = True
    S = input()[::-1]
    cnt = {'W': 0, 'G': 0, 'R': 0}
    for j in range(len(S)):
        if S[j] == 'R':
            cnt['R'] += 1
        if S[j] == 'G':
            if cnt['R'] > 0:
                cnt['R'] -= 1
                cnt['G'] += 1
            else:
                possible = False
        if S[j] == 'W':
            if cnt['G'] > 0:
                cnt['G'] -= 1
                cnt['W'] += 1
            elif cnt['W'] == 0:
                possible = False
    if cnt['R'] > 0 or cnt['G'] > 0:
        possible = False
    if possible:
        print('possible')
    else:
        print('impossible')
