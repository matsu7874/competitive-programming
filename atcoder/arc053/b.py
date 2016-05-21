s = input()
n = [0 for i in range(26)]
for c in s:
    n[ord(c) - ord('a')] += 1
a = 0
b = 0
for i in range(26):
    if n[i] % 2 == 1:
        a += 1
    b += n[i] // 2
if a == 0:
    print(len(s))
else:
    print(1 + b // a * 2)
