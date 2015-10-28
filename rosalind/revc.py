s = input()
sc = ''
for c in s[::-1]:
    if c == 'A':
        sc += 'T'
    elif c == 'T':
        sc += 'A'
    elif c == 'C':
        sc += 'G'
    elif c == 'G':
        sc += 'C'
print(sc)
