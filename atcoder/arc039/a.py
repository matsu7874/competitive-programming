A, B = map(int, input().split())
if A > 899 and B < 200:
    if A > 989 and B < 110:
        print(A - B + max(abs(9 - A % 10), abs(B % 10)))
    else:
        print(A - B + max(abs(9 - A % 100 // 10), abs(B % 100 // 10)) * 10)
else:
    print(A - B + max(abs(9 - A // 100), abs(B // 100) - 1) * 100)
