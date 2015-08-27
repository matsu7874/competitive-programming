import decimal
D = int(input())
N = int(input())
W = [input() for i in range(N)]
def point(s):
    cs = {'O':0, 'D':0, 'I':1, 'Z':2, 'E':3, 'h':4, 's':5, 'q':6, 'L':7, 'B':8, 'G':9}
    pt = 0
    for c in s[::-1]:
        pt *= 10
        pt += cs[c]
    if s[-1] == 'O' or s[-1] == 'D':
        pt = decimal.Decimal(pt / 10**(len(s)-1))
    return pt

# s = 'hELLO'
# print(round(point(s),len(s)))

PT = [0 for i in range(D+1)]
for w in W:
    PT[len(w)] = max(PT[len(w)], point(w))

PT = [PT[i] for i in range(D+1)]
for i in range(1,D+1):
    for j in range(1,i):
        if PT[i-j] >= 1:
            if PT[j] >= 1:
                PT[i] = max(PT[i], PT[i-j]*(10**j)+PT[j])
            else:
                PT[i] = max(PT[i], PT[i-j]*(10**j)+PT[j]*(10**(j-1)))
        else:
            if PT[j] >= 1:
                PT[i] = max(PT[i], PT[i-j]+PT[j]/(10**(i-1)))
            else:
                PT[i] = max(PT[i], PT[i-j]+PT[j]/(10**(i-2)))
print(PT[D])
