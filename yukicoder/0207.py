def is_contain_3(n):
    while n > 0:
        if n % 10 == 3:
            return True
        n //= 10
    return False

A, B = map(int, input().split())

for i in range(A, B + 1):
    if i%3==0 or is_contain_3(i):
        print(i)
