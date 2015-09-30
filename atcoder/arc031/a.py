def is_palindrome(s):
    # 回文判定
    length = len(s)
    for i in range((length+1)//2):
        if s[i] != s[length-1-i]:
            return False
    return True

s=input()
if is_palindrome(s):
    print('YES')
else:
    print('NO')
