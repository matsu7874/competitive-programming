(xa, ya, xb, yb, xc, yc) = map(int, input().split())
S = 0.5 * (abs((xa-xc)*(yb-yc) - (xb-xc)*(ya-yc)))
print(S)
