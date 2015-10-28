s = list(map(int, input().split()))
s.sort()
total = s[0]
for i in range(3):
    s[i] -= total
while s[1] > 0 and s[2] > 0 and (s[1] > 2 or s[2] > 2):
    if s[1] > s[2]:
        total += 1
        s[1] -= 3
        s[2] -= 1
    else:
        total += 1
        s[1] -= 1
        s[2] -= 3
s.sort()
total += s[2]//5
print(total)
