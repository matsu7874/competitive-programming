def prime_sieve(n):
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


def frank(n):
    res = 0
    while n > 0:
        res += n % 10
        n //= 10
    if res > 9:
        return frank(res)
    return res

K = int(input())
N = int(input())
P = prime_sieve(N)
i = 0
while P[i] < K:
    i += 1
P = P[i:]


prime_len = len(P)
H = [frank(p) for p in P]
head = 0
tail = 0
S = set()
ans_l = 0
ans_t = P[0]
while tail <= head < prime_len:
    S.add(H[head])
    # print(P[tail],P[head],(head - tail + 1),S)
    if len(S) == (head - tail + 1):
        if (head - tail + 1) >= ans_l:
            ans_l = (head - tail + 1)
            ans_t = P[tail]
        head += 1
    else:
        if H[head] != H[tail]:
            S.remove(H[tail])
        tail += 1
print(ans_t)
