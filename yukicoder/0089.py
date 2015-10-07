C = int(input())
Rin, Rout = map(int, input().split())
PI = 3.14159265358979
R = (Rin + Rout) / 2
r = (Rout - Rin) / 2
S = r * r * PI
V = 2 * PI * R * S
print(C * V)
