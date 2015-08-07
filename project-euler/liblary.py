def sum_arithmetic_sequence(a, d, n):
    return n*a + (n-1)*n*d//2

def sum_geometric_sequence(a, r, n):
    if r == 0:
        return a
    return a * (1-r**n) / (1-r)

def factrial(n):
    res = 1
    while n > 1:
        res *= n
        n -= 1
    return res

def combination(n, r):
    res = 1
    t = r-1
    while t >= 0:
        res = res*(n-t)//(r-t)
        t -= 1
    return res

def gcd(a, b):
    while b > 0:
        a,b = b, a%b
    return a

def lcm(a, b):
    return a*b // gcd(a,b)

def is_prime(n):
    if n == 2:
        return True
    elif n<2 or n%2==0:
        return False
    for i in range(3, int(n**0.5)+1, 2):
        if n%i == 0:
            return False
    return True

def prime_sieve(n):
    is_prime = [True for i in range(n+1)]
    is_prime[0] = False
    is_prime[1] = False
    for i in range(4, n+1, 2):
        is_prime[i] = False
    for i in range(3, int(n**0.5+1), 2):
        if is_prime[i]:
            for j in range(i*i, n+1, i):
                is_prime[j] = False
    return [i for i in range(n+1) if is_prime[i]]

def prime_decomposition(n, sorted_prime_list=[]):
    prime_factors = []
    if n<2:
        return prime_factors
    if sorted_prime_list == []:
        while n >= 2 and n%2 == 0:
            prime_factors.append(2)
            n //= 2
        i = 3
        while i*i <= n:
            if n%i == 0:
                prime_factors.append(i)
                n //= i
            else:
                i += 2
    else:
        i = 0
        while sorted_prime_list[i]**2 <= n:
            if n%sorted_prime_list[i] == 0:
                prime_factors.append(sorted_prime_list[i])
                n //= sorted_prime_list[i]
            else:
                i += 1
    if n > 1:
        prime_factors.append(n)
    return prime_factors

def get_degree(lst):
    degree = {}
    for i in lst:
        degree.update({i:lst.count(i)})
    return degree

def count_factor(prime_degree):
    res = 1
    for p,v in prime_degree.items():
        res *= v+1
    return res

def each_digits(n, base=10):
    digits = []
    a = 1
    while n >= a:
        digits.append(n//a % base)
        a *= base
    return digits[::-1]

def is_palindromic(n, base=10):
    a = []
    i = 0
    while n>0:
        a.append(n%base**(i+1)//base**i)
        n //= 10
    l = len(a)
    if all([a[i]==a[l-i-1] for i in range(l//2)]):
        return True
    else:
        return False


DAYS_IN_MONTH = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
NAME_OF_MONTH['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

def day_of_week(y, m, d):
    # Zeller's congruence
    # DAY_OF_WEEK = ['Saturday', 'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
    if m == 1 or m == 2:
        m += 12
        y -= 1
    h = (y + y//4 - y//100 + y//400 + (13*m+8)//5 + d) % 7
    return h

def is_leap_year(y):
    if y%4 == 0:
        if y%100 == 0:
            if y%400 == 0:
                return True
            return False
        return True
    return False
































if __name__ == '__main__':
    print(prime_sieve(100))
