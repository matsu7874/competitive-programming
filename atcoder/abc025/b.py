N, A, B = map(int, input().split())
pos = 0
direction = ['East', 'West']
for i in range(N):
    s, d = input().split()
    d = max(A, min(B, int(d)))
    pos += (-1)**direction.index(s) * d
if pos < 0:
    print('West', -pos)
elif pos == 0:
    print(0)
else:
    print('East', pos)
