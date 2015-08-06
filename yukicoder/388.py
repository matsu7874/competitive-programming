x,y,r = [int(x) for x in input().split()]
x = max(x,-x)
y = max(y,-y)
print(int(x+y+r*(2**0.5)+1))