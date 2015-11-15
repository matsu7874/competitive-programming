DAYS_IN_MONTH = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
NAME_OF_MONTH = ['January', 'February', 'March', 'April', 'May', 'June',
                 'July', 'August', 'September', 'October', 'November', 'December']
DAY_OF_WEEK = ['Sunday', 'Monday', 'Tuesday',
               'Wednesday', 'Thursday', 'Friday', 'Saturday']


def is_palindrome(s):
    # 回文判定
    length = len(s)
    for i in range((length + 1) // 2):
        if s[i] != s[length - 1 - i]:
            return False
    return True


def sum_arithmetic_sequence(a, d, n):
    # 等差数列の和の公式
    return n * a + (n - 1) * n * d // 2


def sum_geometric_sequence(a, r, n):
    # 等比数列の和の公式
    if r == 0:
        return a
    return a * (1 - r**n) / (1 - r)


def factrial(n):
    # 階乗
    res = 1
    while n > 1:
        res *= n
        n -= 1
    return res


def combination(n, r):
    # 組み合わせ
    res = 1
    t = r - 1
    while t >= 0:
        res = res * (n - t) // (r - t)
        t -= 1
    return res


def gcd(a, b):
    # 最小公倍数
    while b > 0:
        a, b = b, a % b
    return a


def lcm(a, b):
    # 最大公約数
    return a * b // gcd(a, b)


def is_prime(n):
    # 素数判定
    if n == 2:
        return True
    elif n < 2 or n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


def prime_sieve(n):
    # 素数リスト(エラトステネスの篩)
    is_prime = [True for i in range(n + 1)]
    is_prime[0] = False
    is_prime[1] = False
    for i in range(4, n + 1, 2):
        is_prime[i] = False
    for i in range(3, int(n**0.5 + 1), 2):
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False
    return [i for i in range(n + 1) if is_prime[i]]


def prime_decomposition(n, sorted_prime_list=[]):
    # 素因数分解
    prime_factors = []
    if n < 2:
        return prime_factors
    if sorted_prime_list == []:
        while n >= 2 and n % 2 == 0:
            prime_factors.append(2)
            n //= 2
        i = 3
        while i * i <= n:
            if n % i == 0:
                prime_factors.append(i)
                n //= i
            else:
                i += 2
    else:
        i = 0
        while sorted_prime_list[i]**2 <= n:
            if n % sorted_prime_list[i] == 0:
                prime_factors.append(sorted_prime_list[i])
                n //= sorted_prime_list[i]
            else:
                i += 1
    if n > 1:
        prime_factors.append(n)
    return prime_factors


def get_divisors(n):
    # 約数列挙
    divisors = set()
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            divisors.add(i)
            divisors.add(n // i)
    return list(divisors)


def get_frequency(lst):
    frequency = {}
    for i in lst:
        frequency.update({i: lst.count(i)})
    return frequency


def count_factor(prime_frequency):
    res = 1
    for p, v in prime_frequency.items():
        res *= v + 1
    return res


def each_digits(n, base=10):
    # 各桁の数字を得る
    digits = []
    a = 1
    while n >= a:
        digits.append(n // a % base)
        a *= base
    return digits[::-1]


def is_palindromic(n, base=10):
    # 回文数判定
    a = []
    i = 0
    while n > 0:
        a.append(n % base**(i + 1) // base**i)
        n //= 10
    l = len(a)
    if all([a[i] == a[l - i - 1] for i in range(l // 2)]):
        return True
    else:
        return False


def day_of_week(y, m, d):
    # 曜日を得る(ツェラーの公式)
    # 日曜日が0,土曜日が6
    # Zeller's congruence
    if m == 1 or m == 2:
        m += 12
        y -= 1
    h = (y + y // 4 - y // 100 + y // 400 + (13 * m + 8) // 5 + d) % 7
    return h


def is_leap_year(y):
    # うるう年判定
    if y % 4 == 0:
        if y % 100 == 0:
            if y % 400 == 0:
                return True
            return False
        return True
    return False


def days_since_epoch(year, month, day):
    # 1年1月1日からの経過日数を求める
    # days_since_epoch(1,1,1)=0
    DAYS_IN_MONTH = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    cnt = day - 1
    for i in range(month - 1):
        cnt += DAYS_IN_MONTH[i]
    cnt += 365 * (year - 1)
    if month <= 2:
        y = year - 1
    else:
        y = year
    cnt += y // 4
    cnt -= y // 100
    cnt += y // 400
    return cnt


def lower_bound(lst, n):
    # ソートされたlst内でlst[index]がn以上かつ最小のindexを返す
    # nを挿入する際にソートが維持される最小のindexを返す
    l = 0
    r = len(lst)
    while l < r:
        m = (l + r) // 2
        if lst[m] >= n:
            r = m
        elif lst[m] < n:
            l = m + 1
    return l


def upper_bound(lst, n):
    # ソートされたlst内でlst[index]がn以下かつ最大のindexを返す
    # nを挿入する際にソートが維持される最大のindexを返す
    l = 0
    r = len(lst)
    while l < r:
        m = (l + r) // 2
        if lst[m] > n:
            r = m - 1
        elif lst[m] <= n:
            l = m + 1
    return l


class UnionFind:

    def __init__(self, size):
        # 負の値はルート (集合の代表) で集合の個数
        # 正の値は次の要素を表す
        self.table = [-1 for _ in range(size)]

    def find(self, x):
        # 集合の代表を求める
        while self.table[x] >= 0:
            x = self.table[x]
        return x

    def union(self, x, y):
        # 併合
        s1 = self.find(x)
        s2 = self.find(y)
        if s1 != s2:
            if self.table[s1] >= self.table[s2]:
                self.table[s1] += self.table[s2]
                self.table[s2] = s1
            else:
                self.table[s2] += self.table[s1]
                self.table[s1] = s2
        return self.table[s1]


# 幾何

EPS = 10**-8
INF = 10**12


def ccw(ax, ay, bx, by, cx, cy):
    bx -= ax
    cx -= ax
    by -= ay
    cy -= ay


def distance(px, py, qx, qy):
    return ((px - qx) * (px - qx) + (py - qy) * (py - qy))**0.5


def distance2(px, py, qx, qy):
    return (px - qx) * (px - qx) + (py - qy) * (py - qy)


def signed_area(ax, ay, bx, by, cx, cy):
    return ((bx - ax) * (cy - ay) - (by - ay) * (cx - ax)) * 0.5

if __name__ == '__main__':
    lst = [1, 2, 2, 4, 5, 5, 5, 7, 7, 8, 1000]
    print(lst)
    n = int(input())
    print(lower_bound(lst, n), upper_bound(lst, n))
