n=int(input())
max_s = 'atcoder'
max_p = 0
total_p = 0
for i in range(n):
    s,p = input().split()
    total_p += int(p)
    if int(p) > max_p:
        max_s = s
        max_p = int(p)
if max_p*2 > total_p:
    print(max_s)
else:
    print('atcoder')
