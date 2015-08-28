N = input()
digit = [n for n in N]
digit.sort()
print(''.join(digit[::-1]))
