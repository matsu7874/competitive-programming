K = int(input())
S = input()
x = 0
y = 0
foot = set()
foot.add((x,y))
for s in S:
    if s == 'L':
        while (x - 1, y) in foot:
            x -= 1
        x -= 1
    elif s == 'R':
        while (x + 1, y) in foot:
            x += 1
        x += 1
    elif s == 'U':
        while (x, y + 1) in foot:
            y += 1
        y += 1
    elif s == 'D':
        while (x, y - 1) in foot:
            y -= 1
        y -= 1
    foot.add((x,y))
print(x,y)
