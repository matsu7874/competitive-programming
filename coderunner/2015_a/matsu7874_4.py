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
N=1200
A=[]
for i in range(N):
    a,b=map(int, input().split())
    A.append((a,b))
for i in range(10,N):
    ps = [A[i][0],A[i][1]]
    for j in range(1,120):
        a,b=A[i+j]
        if a not in ps and b not in ps:
            ps.append(a)
            ps.append(b)
            qu = ','.join([str(c) for c in ps])
            result = question(qu)
            if result <= 0:
                ps.pop()
                ps.pop()
            f = open('log3.txt', 'a')
            f.write(qu + ' ' + str(result) + '\n')
            f.close()
            print(qu + ' ' + str(result))
            time.sleep(1)
