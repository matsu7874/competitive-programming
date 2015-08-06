N = int(input())
minimum = 36**13
def alf_num(c):
    if ord(c)>=ord('A'):
        return 10+ord(c)-ord('A')
    else:
        return int(c)
def f(s):
    l = len(s)
    base = 1
    for i in range(ord('1'),ord('9')+1):
        if chr(i) in s:
            base = alf_num(chr(i))
    for i in range(ord('A'),ord('Z')+1):
        if chr(i) in s:
            base = alf_num(chr(i))
    sum = 0
    for i in range(l):
        sum += alf_num(s[l-1-i])*((base+1)**i)
    return sum
for _ in range(N):
    V = input()
    minimum = min(minimum, f(V))
print(minimum)
