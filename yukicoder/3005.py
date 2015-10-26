import hashlib
cnt = 0
s = 'yukicoder'
while True:
    s = hashlib.md5(s.encode('utf-8')).hexdigest()
    cnt += 1
    if s == 'bdb0cafdae8666d1361b03db938d722f':
        break
s = input()
for i in range(cnt):
    s = hashlib.md5(s.encode('utf-8')).hexdigest()
print(s)
