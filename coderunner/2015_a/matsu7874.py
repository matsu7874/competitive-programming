import urllib.request
import time
import itertools


token = 'Z35DXNLA8EHC2ECG12N595EF7FW1LEDC'


def query(url):
    res = urllib.request.urlopen(url)
    return res.read()


def question(s):
    url = 'https://game.coderunner.jp/query?token=?token=' + \
        token + '&v=' + s
    result = query(url)
    print(s + ' ' + result.decode("utf-8"))
    return int(result.decode("utf-8"))
print('GO')
while True:
    for i in range(3, 500):
        for s in itertools.permutations(range(1000), r=i * 2):

            S=','.join([str(c) for c in s])
            url = 'https://game.coderunner.jp/query?token=' + token + '&v=' + S
            f = open('log.txt', 'a')
            result = query(url)
            f.write(S + ' ' + result.decode("utf-8") + '\n')
            f.close()
            print(S + ' ' + result.decode("utf-8"))
            time.sleep(1)
