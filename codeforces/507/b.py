import math
(r,xa,ya,xb,yb) = [int(x) for x in input().split()]
print(int(math.ceil(math.sqrt((xb-xa)**2+(yb-ya)**2)/(2*r))))
