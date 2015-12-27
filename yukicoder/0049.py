S=input() + ';'
left = 0
term = 0
i = 0
op = ''
for c in S:
    if c in ('0123456789'):
        term *= 10
        term += int(c)
    else:
        if op == '+':
            left *= term
        elif op == '*':
            left += term
        else:
            left = term
        term = 0
        op = c
print(left)
