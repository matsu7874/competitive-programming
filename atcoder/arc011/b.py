N = int(input())
S = input().lower()
table = {'b': 1, 'c': 1, 'd': 2, 'w': 2, 't': 3, 'j': 3, 'f': 4, 'q': 4, 'l': 5, 'v': 5,
         's': 6, 'x': 6, 'p': 7, 'm': 7, 'h': 8, 'k': 8, 'n': 9, 'g': 9, 'z': 0, 'r': 0}
for c in 'aeiouy,.':
    S = S.replace(c, '')
while '  ' in S:
    S = S.replace('  ', ' ')
ans = ''
for c in S.strip():
    if c == ' ':
        ans += ' '
    else:
        ans += str(table[c])
print(ans)
