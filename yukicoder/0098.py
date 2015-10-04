import math
Xp, Yp = map(int, input().split())
r = math.ceil((Xp * Xp + Yp * Yp)**0.5 * 2)
if Xp * Xp + Yp * Yp == r * r / 4:
    r += 1
print(r)
