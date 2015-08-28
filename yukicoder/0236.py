A, B, X, Y = map(int, input().split())
if X * B < Y * A:
    print(X + (X * B) / A)
else:
    print(Y + (Y * A) / B)
