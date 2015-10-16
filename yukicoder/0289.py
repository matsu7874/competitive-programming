s=input()
total = 0
for c in s:
    if c in '123456789':
        total += int(c)
print(total)
