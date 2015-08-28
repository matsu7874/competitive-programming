def is_palindrome(s):
    if s == s[::-1]:
        return True
    else:
        return False


def longest_palindrome_length(s):
    n = len(s)
    i = 0
    j = 0
    max_rad = 0
    rad = [0 for i in range(2 * n)]
    while i < 2 * n:
        while 0 <= i - j and i + j + 1 < 2 * n and s[(i - j) // 2] == s[(i + j + 1) // 2]:
            j += 1
        rad[i] = j
        max_rad = max(max_rad, j)
        k = 1
        while 0 <= i - k and 0 <= rad[i] - k and rad[i - k] < rad[i] - k:
            rad[i + k] = min(rad[i - k], rad[i] - k)
            k += 1
        i += k
        j = max(j - k, 0)
    print(max_rad)

S = input()
if is_palindrome(S):
    longest_palindrome_length(S[1:])
else:
    longest_palindrome_length(S)
