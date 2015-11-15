import urllib.request
import time
import itertools
import random


def query(url):
    time.sleep(1)
    res = urllib.request.urlopen(url)
    return res.read()


def question(s):
    url = 'http://sample.coderunner.jp/q?token=' + \
        token + '&str=' + s
    result = query(url)
    print(s + ' ' + result.decode("utf-8"))
    return int(result.decode("utf-8"))

token = 'scce5MmDrK33j1pK3SswjrdRDxKnr18A'


def best_first_beam_search():
    S = ['']
    T = set()
    P = []
    for i in range(50):
        for s in S:
            for j in range(20):
                r = random.randint(0, len(s))
                T.add(s[:r] + random.choice(['A', 'B', 'C', 'D']) + s[r:])
        for t in T:
            P.append((question(t), t))
        P.sort()
        P.reverse()
        S = []
        T = set()
        for i in range(3):
            S.append(P[i][1])

def rc():
    return random.choice(['A', 'B','C', 'D'])

def ttt():
    print('go')
    S = 'CBCBCBDCACBBBBBADACBCBBDCCCDADAACDDDCBABADCBBDADBA'
    max_p = 1818
    while True:
        r = random.randint(0, 47)

        s = S[:r] + ''.join([rc() for i in range(3)]) + S[r + 3:]
        p = question(s)
        if max_p < p:
            S = s
            max_p = p

ttt()
