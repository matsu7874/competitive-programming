L = int(input())
M = int(input())
N = int(input())
if N >= 25:
    M += N // 25
    N %= 25
if M >= 4:
    L += M // 4
    M %= 4
L %= 10
print(L + M + N)
