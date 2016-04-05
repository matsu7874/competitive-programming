s = input()
c = [0 for i in range(len(s))]
w = [0 for i in range(len(s))]
for i in range(len(s)):
    if s[i] == 'c':
        c[i] += 1
    elif s[i] == 'w':
        w[i] += 1
for i in range(1, len(s)):
    c[i] += c[i - 1]
for i in range(len(s) - 2, 0, -1):
    w[i] += w[i + 1]
total = 0
for i in range(1, len(s) - 1):
    if s[i] == 'w':
        total += c[i - 1] * w[i + 1]
print(total)
