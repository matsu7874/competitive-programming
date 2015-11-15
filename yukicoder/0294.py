def generate
def is_SuperFizzBuzz(n):
    while n:
        d = n % 10
        if d == 3 or d == 5:
            n //= 10
        else:
            return False
    return True

N = int(input())

i = 1
cnt = 0
while True:
    if is_SuperFizzBuzz(15 * i):
        cnt += 1
        if cnt == N:
            print(15 * i)
            break
    i += 1
