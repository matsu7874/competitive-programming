def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

T = [int(input()) for i in range(3)]
g = lcm(lcm(T[0],T[1]),T[2])
S = [g//T[i] for i in range(3)]
den = 0
for i in range(1,g//min(S)+1):
    if S[0]%i == S[1]%i and S[1]%i == S[2]%i:
        den = i

print(str(g//gcd(g,den))+'/'+str(den//gcd(g,den)))
