def evaluate(s):
    v = 0
    t = 0
    op = 1
    for c in s:
        if c == '+':
            v += op * t
            op = 1
            t = 0
        elif c == '-':
            v += op * t
            op = -1
            t = 0
        else:
            t = t * 10 + int(c)
    else:
        v += op * t
    return v

S = input()
L = len(S)
max_v = -999999999
for i in range(L):
    s = S[i:] + S[:i]
    if s[0] in '+-' or s[-1] in '+-':
        continue
    max_v = max(max_v, evaluate(s))
print(max_v)
