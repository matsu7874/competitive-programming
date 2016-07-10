def is_kadomatsu(a, b, c):
    return (a < c < b or b < a < c or b < c < a or c < a < b)

a = list(map(int, input().split()))
if is_kadomatsu(*a):
    print('INF')
else:
    cnt = 0
    for p in range(1, max(a) + 1):
        if is_kadomatsu(*[e % p for e in a]):
            cnt += 1
    print(cnt)
