import itertools
def ab(a,b,n):
    if n == 0:
        return ''
    return (a+b)*n
def is_safe(a, b):
    out = {
        'R': 'ORV',
        'V': 'ORVBG',
        'B': 'VBG',
        'G': 'VBGYO',
        'Y': 'GYO',
        'O': 'GYORV'
    }
    return b not in out[a]

def solve(n, r, o, y, g, b, v):
    if b==o and r==0 and y==0 and g==0 and v==0:
        return ab('B','O', b)
    elif r==g and b==0 and y==0 and o==0 and v==0:
        return ab('R','G', r)
    elif y==v and r==0 and b==0 and g==0 and o==0:
        return ab('Y','V', y)
    elif 0<b<=o or 0<r<=g or 0<y<=v:
        return 'IMPOSSIBLE'
    
    bob = rgr = yvy = ''
    if b > 0:
        b -= o+1
        bob = ab('B', 'O', o) + 'B'
    if r > 0:
        r -= g+1
        rgr = ab('R', 'G', g) + 'R'
    if y > 0:
        y -= v+1
        yvy = ab('Y', 'V', v) + 'Y'
    
    if b > r+y+1 or r > b+y+1 or y > b+r+1:
        return 'IMPOSSIBLE'
    tmp = []
    U = [[b, 'B'], [r, 'R'], [y, 'Y']]
    U.sort(reverse=True)
    cnt = U[1][0] - U[2][0]
    tmp.append(ab(U[0][1], U[1][1], cnt))
    U[0][0] -= cnt
    U[1][0] -= cnt
    # print(U)
    if U[0][0] >= 2:
        cnt = min(U[0][0]//2, U[0][0] - U[1][0])
        tmp.append(ab(U[0][1]+U[1][1], U[0][1]+U[2][1], cnt))
        U[0][0] -= cnt * 2
        U[1][0] -= cnt
        U[2][0] -= cnt
    # print(U)
    
    tmp.append((U[0][1]+U[1][1]+U[2][1]) * U[2][0])
    U[0][0] -= U[2][0]
    U[1][0] -= U[2][0]
    U[2][0] -= U[2][0]
    # print(U)

    if U[0][0] > 0:
        tmp.append(U[0][1])
        U[0][0] -= 1
    # print(U)
    
    if any([U[i][0] > 0 for i in range(3)]):
        print(U)
    cnd = []
    if bob:
        cnd.append(bob)
    if rgr:
        cnd.append(rgr)
    if yvy:
        cnd.append(yvy)
    ret = ''.join(tmp)
    if ret:
        cnd.append(ret)
    
    for pt in itertools.permutations(range(len(cnd))):
        # print(''.join([cnd[pt[i]] for i in range(len(cnd))]))
        if all([is_safe(cnd[pt[i]][-1], cnd[pt[i+1]][0]) for i in range(len(cnd)-1)]) and is_safe(cnd[pt[0]][0], cnd[pt[-1]][-1]):
            return ''.join([cnd[pt[i]] for i in range(len(cnd))])
    return 'IMPOSSIBLE'
    # if ret == '':
    #     return  bob + rgr + yvy
    
    # head = ret[0]
    # tail = ret[-1]

    # if head == 'B' and tail == 'B':
    #     if rgr == '' or yvy == '':
    #         ans = 'IMPOSSIBLE'
    #     else:
    #         ans = bob + rgr + ret + yvy
    # elif head == 'B' and tail == 'R':
    #     if rgr == '' or yvy == '':
    #         ans = 'IMPOSSIBLE'
    #     slif rgr  == '':

    #     ans = bob + rgr + ret +  yvy
    # elif head == 'B' and tail == 'Y':
    #     ans = bob + rgr + yvy + ret
    # elif head == 'R' and tail == 'B':
    #     ans = bob + ret + rgr + yvy
    # elif head == 'R' and tail == 'R':
    #     ans = bob + rgr + yvy + ret
    # elif head == 'R' and tail == 'Y':
    #     ans = bob + rgr + yvy + ret
    # elif head == 'Y' and tail == 'B':
    #     ans = bob + rgr + ret +  yvy
    # elif head == 'Y' and tail == 'R':
    #     ans = bob + rgr + ret + yvy
    # elif head == 'Y' and tail == 'Y':
    #     ans = bob + ret + rgr + yvy
    # if ans[0] == ans[-1]:
    #     return 'IMPOSSIBLE'
        
    # return ans
import collections
def check(N,R,O,Y,G,B,V, ans):
    if ans == 'IMPOSSIBLE':
        return
    if len(ans) != N:
        print('len(ans) != N', len(ans), N)
    cnt = collections.Counter(ans)
    if(cnt['R']!=R):
        print('R', cnt['R'],R)
    if(cnt['O']!=O):
        print('O',cnt['O'],O)
    if(cnt['Y']!=Y):
        print('Y',cnt['Y'],Y)
    if(cnt['G']!=G):
        print('G', cnt['G'],G)
    if(cnt['B']!=B):
        print('B', cnt['B'],B)
    pre = '_'
    for i in range(len(ans)):
        c = ans[i]
        if c == 'B' and pre in 'GBV':
            print(i)
        elif c == 'Y' and pre in 'OYG':
            print(i)
        elif c == 'R' and pre in 'VRO':
            print(i)
        pre = c




def print_answer(t, ans):
    tmpl = 'Case #{0}: {1}'
    print(tmpl.format(t+1, ans))

if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        N,R,O,Y,G,B,V = map(int, input().split())
        ans = solve(N,R,O,Y,G,B,V)
        print_answer(_, ans)
        check(N,R,O,Y,G,B,V, ans)