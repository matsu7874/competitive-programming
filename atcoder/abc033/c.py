s = list(input().split('+'))
total = 0
for i in range(len(s)):
    if '0' not in s[i]:
        total += 1
print(total)
