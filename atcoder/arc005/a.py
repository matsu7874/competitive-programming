N = int(input())
W = input().split()
total = 0
for w in W:
    if w in ['TAKAHASHIKUN', 'Takahashikun', 'takahashikun', 'TAKAHASHIKUN.', 'Takahashikun.', 'takahashikun.']:
        total += 1
print(total)
