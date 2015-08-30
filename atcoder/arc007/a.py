X = input()
S = [x for x in input()]
while X in S:
    S.remove(X)
print(''.join(S))
