def distance(px, py, qx, qy):
    dx = px - qx
    dy = py - qy
    return (dx * dx + dy * dy)**0.5

N = int(input())
P = []
for i in range(N):
    x, y = map(int, input().split())
    P.append((x, y))
longest_line = 0
for p in P:
    for q in P:
        longest_line = max(longest_line, distance(p[0], p[1], q[0], q[1]))
print(longest_line)
