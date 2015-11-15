S = input()

cnt = [[10000,chr(ord('a')+i)] for i in range(ord('z')-ord('a')+1)]

for s in S:
    cnt[ord(s)-ord('a')][0] -= 1
cnt.sort()
for i in range(3):
    print(cnt[i][1], 10000-cnt[i][0])
