def is_palindrome(s):
    # 回文判定
    length = len(s)
    for i in range((length + 1) // 2):
        if s[i] != s[length - 1 - i]:
            return False
    return True

A = input()
N = len(A)
not_same = []
total = 0
for i in range((N + 1) // 2):
    if A[i] != A[N - 1 - i]:
        not_same.append(i)
n = len(not_same)
if n == 0:
    total = N // 2 * 50
elif n == 1:
    if N % 2 == 0:
        total = N * 25 - 2
    else:
        if (N + 1) // 2 in not_same:
            total = N * 25 - 1
        else:
            total = N * 25 - 2
else:
    total = 25*N
print(total)
