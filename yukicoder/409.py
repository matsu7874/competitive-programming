S = input()

def factorial(n):
    ans = 1
    while n>1:
        ans *= n
        n -= 1
    return ans
ans = factorial(len(S))
for i in range(ord('A'),ord('Z')+1):
    ans //= factorial(S.count(chr(i)))
print(ans-1)