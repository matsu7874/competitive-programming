DAYS_IN_MONTH = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
NAME_OF_MONTH = ['January', 'February', 'March', 'April', 'May', 'June',
                 'July', 'August', 'September', 'October', 'November', 'December']
DAY_OF_WEEK = ['Sunday', 'Monday', 'Tuesday',
               'Wednesday', 'Thursday', 'Friday', 'Saturday']

def mod_pow(x, n, mod):
    # (x**n)%mod を返す
    res = 1
    while n > 0:
        if n & 1:
            res = res * x % mod
        x = x * x % mod
        n //= 2
    return res

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
    # 最大公約数
    while b > 0:
        a, b = b, a % b
    return a


def lcm(a, b):
    # 最小公倍数
    return a * b // gcd(a, b)


def get_divisors(n):
    # 約数列挙
    # リストがソートされていないことに注意せよ。
    divisors = set()
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            divisors.add(i)
            divisors.add(n // i)
    return list(divisors)


def Eulers_Phi_Function(n):
    freq = collections.Counter(prime_decomposition(n))
    ans = n
    for k,v in freq.items():

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


def maxBy(f, x, y):
    if f(x) > f(y):
        return x
    else:
        return y


def lcs(a, b, dic):
    if (a, b) in dic:
        return dic[(a, b)]
    if a == '' or b == '':
        ret = ''
    elif a[-1] == b[-1]:
        ret = lcs(a[:-1], b[:-1], dic) + a[-1]
    else:
        lcs_a = lcs(a[:-1], b, dic)
        lcs_b = lcs(a, b[:-1], dic)
        if len(lcs_a) > len(lcs_b):
            ret = lcs_a
        else:
            ret = lcs_b
    dic[(a, b)] = ret
    return ret




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
