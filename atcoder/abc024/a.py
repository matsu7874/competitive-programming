a,b,c,k = [int(x) for x in input().split()]
s,t = [int(x) for x in input().split()]
if s+t>=k:
    print(a*s+b*t-c*(s+t))
else:
    print(a*s+b*t)