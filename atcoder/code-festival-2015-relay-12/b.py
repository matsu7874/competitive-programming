P = [input() for i in range(10)]
if all(any(P[j][i] == 'o' for j in range(10))for i in range(10)):
    print('Yes')
else:
    print('No')
