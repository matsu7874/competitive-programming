import urllib.request
import time
import itertools
import random


token = 'Z35DXNLA8EHC2ECG12N595EF7FW1LEDC'


def query(url):
    res = urllib.request.urlopen(url)
    return res.read()


def question(s):
    url = 'https://game.coderunner.jp/query?token=' + token + '&v=' + s
    result = query(url)
    return int(result.decode("utf-8"))

print('GO')
N = 28
max_p = 0
PS = []
for i in range(1200):
    p = random.randint(0, 999)
    q = random.randint(0, 999)
    qu = str(p) + ',' + str(q)
    result = question(qu)
    if result > 0:
        max_p = result
        PS.append((result, p, q))
    f = open('log2.txt', 'a')
    f.write(qu + ' ' + str(result) + '\n')
    f.close()
    print(qu + ' ' + str(result))
    time.sleep(1)
PS.sort()
PS.reverse()
lps=len(PS)
for i in range(2,min(lps,500)):
    for j in range(60):
        ps=random.sample(PS,i)
    qu = ','.join([str(ps[k][0])+','+str(ps[k][1]) for k in range(i)])
    result = question(qu)
    if result > 0:
        max_p = result
        PS.append((result, p, q))
    f = open('log3.txt', 'a')
    f.write(qu + ' ' + str(result) + '\n')
    f.close()
    print(qu + ' ' + str(result))
    time.sleep(1)


while True:
    for s in S:
        for i in range(10):
            r = random.randint(0, N - 2)
            t = s[1][:r] + \
                [random.randint(0, 999), random.randint(0, 999)] + s[1][r + 2:]
            qu = ','.join([str(c) for c in t])
            result = question(qu)
            f = open('log.txt', 'a')
            f.write(qu + ' ' + str(result) + '\n')
            f.close()
            print(qu + ' ' + str(result))
            time.sleep(1)
            if result > max_p:
                max_p = result
                S.append((max_p, t[:]))
        for i in range(10):
            ra = random.randint(0, N // 2 - 2)
            rb = random.randint(N // 2 - 1, N - 2)
            t = s[1][:]
            t[ra:ra + 2], t[rb:rb + 2] = t[rb:rb + 2], t[ra:ra + 2]
            qu = ','.join([str(c) for c in t])
            result = question(qu)
            f = open('log.txt', 'a')
            f.write(qu + ' ' + str(result) + '\n')
            f.close()
            print(qu + ' ' + str(result))
            time.sleep(1)
            if result > max_p:
                max_p = result
                S.append((max_p, t[:]))

    S.sort()
    S.reverse()
    S = S[0:max(len(S), 4)]
