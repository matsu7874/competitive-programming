s =input()
ary = []
for c in s:
    if c == 'B':
        if len(ary) > 0:
            ary.pop()
    else:
        ary.append(c)
print(''.join(ary))