def is_prime(n):
    if n%2==0 or n==1:
        return False
    sqrt_n = int(n**0.5)
    for i in range(3,sqrt_n+2,2):
        if n%i==0:
            return False
    return True

n = int(input())
if is_prime(int((n*(n+1))/2)):
    print('WANWAN')
else:
    print('BOWWOW')
