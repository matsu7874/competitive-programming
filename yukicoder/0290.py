n = int(input())
s = input()
if '00' in s or '11' in s:
    print('YES')
elif n > 3:
    print('YES')
else:
    print('NO')
