a,b,c = [int(x) for x in input().split()]
if a!=b and a!=c:
    print(a)
elif a==b:
    print(c)
else:
    print(b)
