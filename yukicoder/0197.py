S_b = [c for c in input()]
N = int(input())
S_a = [c for c in input()]
o_b = S_b.count('o')
o_a = S_a.count('o')

if o_b!=o_a:
    print('SUCCESS')
    exit()
if o_b==0 or o_b == 3:
    print('FAILURE')
    exit()

t = 'o'
if o_b == 2:
    t = 'x'

d = abs(S_b.index(t) - S_a.index(t))
if N == 0:
    if S_b != S_a:
        print('SUCCESS')
    else:
        print('FAILURE')
elif N == 1:
    if d == 2 or (d==0 and S_b.index(t)==1):
        print('SUCCESS')
    else:
        print('FAILURE')
else:
    print('FAILURE')
