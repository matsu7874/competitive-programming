import string

N = int(input())
digit = 1
while 26 * (26**digit - 1) // 25 < N + 1:
    digit += 1
S = ''
for i in range(digit):
    n = N - (26 * (26**i - 1) // 25)
    S += string.ascii_uppercase[n % (26**i * 26) // (26**i)]
S = S[::-1]
T = string.ascii_uppercase[N % 26]
print(S[:-1] + T)


exit()
