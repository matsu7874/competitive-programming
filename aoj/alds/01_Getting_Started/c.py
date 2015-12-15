def is_prime(n):
    # 素数判定
    if n == 2:
        return True
    elif n < 2 or n & 1 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

N = int(input())
cnt = 0
for i in range(N):
    e = int(input())
    if is_prime(e):
        cnt += 1
print(cnt)
