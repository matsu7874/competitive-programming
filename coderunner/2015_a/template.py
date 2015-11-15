import urllib.request
import time
import itertools


token = 'Z35DXNLA8EHC2ECG12N595EF7FW1LEDC'


def query(url):
    res = urllib.request.urlopen(url)
    return res.read()

def question(s):
    url = 'http://sample.coderunner.jp/q?token=' + \
        token + '&str=' + s
    result = query(url)
    print(s + ' ' + result.decode("utf-8"))
    return int(result.decode("utf-8"))

for i in range(1,50):
	for s in itertools.product(['A','B','C','D'], repeat=i):
		url = 'http://sample.coderunner.jp/q?token=' + token + '&str=' + ''.join(s)
		f = open('log.txt','a')
		result = query(url)
		f.write(''.join(s)+' '+result.decode("utf-8")+'\n')
		f.close()
		print(''.join(s)+' '+result.decode("utf-8"))
		time.sleep(1)
