import re
N = int(input())
CSS = [input() for i in range(N)]
C = '0123456789abcdefABCDEF'
for i in range(N):
    row = re.findall('(?!\A)(#[a-fA-f_0-9]{6}|#[a-fA-f_0-9]{3})', CSS[i])
    if row != []:
        for j in row:
            print(j)
