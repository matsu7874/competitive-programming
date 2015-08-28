import sys
left = 1
right = 10**9
mid = (left + right) // 2
res = 1
last_1_left = 0
while left <= right:
    mid = (left + right) // 2
    print('?', mid)
    sys.stdout.flush()
    res = int(input())
    if res == 1:
        last_1 = mid
        left = mid + 1
    else:
        right = mid - 1
print('!', last_1)
sys.stdout.flush()
