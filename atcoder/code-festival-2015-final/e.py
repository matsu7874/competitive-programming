S = input()
ans = ''
a = S.count('!')
b = S.count('-')
if a >= 1:
    ans += '-' * (S.find('!') % 2)
else:
    ans += '-' * (b % 2)
if a % 2 == 1:
    ans += '!'
elif a > 1:
    ans += '!!'
print(ans)
