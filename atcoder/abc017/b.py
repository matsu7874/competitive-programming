s = input()
if s == '':
    print('YES')
    exit()

s = s.replace('ch', 'X')
s = s.replace('o', 'X')
s = s.replace('k', 'X')
s = s.replace('u', 'X')

if s.count('X') == len(s):
    print('YES')
else:
    print('NO')
