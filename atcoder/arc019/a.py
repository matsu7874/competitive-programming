s = input()
a = ''
for c in s:
    if c == 'O' or c == 'D':
        a += '0'
    elif c == 'I':
        a += '1'
    elif c == 'Z':
        a += '2'
    elif c == 'S':
        a += '5'
    elif c == 'B':
        a += '8'
    else:
        a += c
print(a)
