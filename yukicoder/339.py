S = input()
buff = ''
for c in S:
    if ord('A') <= ord(c) <= ord('Z'):
        buff += chr(ord(c) + (ord('a')-ord('A')))
    else:
        buff += chr(ord(c) - (ord('a')-ord('A')))
print(buff)