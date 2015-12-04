import math


def is_kadomatsu(h):
    return (h[1] > h[0] and h[1] > h[2] and h[0] != h[2]) or (h[1] < h[0] and h[1] < h[2] and h[0] != h[2])

d = int(input())
H = [int(input()) for i in range(3)]
if d == 0:
    if is_kadomatsu(H):
        print(0)
    else:
        print(-1)
    exit()

if is_kadomatsu(H):
    print(0)
    exit()

top = 10**10
bottom = 10**10

h = H[:]
cnt = 0
if h[0] >= h[1]:
    cnt += (h[0] - h[1]) // d
    h[0] = max(0, h[0] - (h[0] - h[1]) // d * d)
    while h[0] >= h[1] > 0:
        cnt += 1
        h[0] = max(0, h[0] - d)
if h[2] >= h[1]:
    cnt += (h[2] - h[1]) // d
    h[2] = max(0, h[2] - (h[2] - h[1]) // d * d)
    while h[2] >= h[1] > 0:
        cnt += 1
        h[2] = max(0, h[2] - d)
if h[0] == h[2]:
    h[0] = max(0, h[0] - d)
    cnt += 1
if is_kadomatsu(h):
    top = cnt

h = H[:]
cnt = 0
if h[0] == h[2]:
    h[0] = max(0, h[0] - d)
    cnt += 1
if h[0] <= h[1]:
    cnt += (h[1] - h[0]) // d
    h[1] = max(0, h[1] - (h[1] - h[0]) // d * d)
    while 0 < h[0] <= h[1]:
        cnt += 1
        h[1] = max(0, h[1] - d)
if h[2] <= h[1]:
    cnt += (h[1] - h[2]) // d
    h[1] = max(0, h[1] - (h[1] - h[2]) // d * d)
    while 0 < h[2] <= h[1]:
        cnt += 1
        h[1] = max(0, h[1] - d)
if is_kadomatsu(h):
    bottom = cnt


if top == bottom == 10**10:
    print(-1)
else:
    print(min(top, bottom))
