S = input()
if len(S) == 2:
    print('dict')
    exit()
level = 0
for c in S:
    if c == '{':
        level += 1
    elif c == '}':
        level -= 1
    if level == 1:
        if c == ':':
            print('dict')
            exit()
        elif c == ',':
            print('set')
            exit()
print('set')
