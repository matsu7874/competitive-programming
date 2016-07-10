import itertools

res = ''
for code in itertools.product([str(i) for i in range(10)], repeat=3):
    print(''.join(code), flush=True)
    res = input()
    if res == 'unlocked':
        exit()
