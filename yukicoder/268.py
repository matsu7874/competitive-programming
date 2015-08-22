import itertools
L = [int(x) for x in input().split()]
C = [int(x) for x in input().split()]

L.sort()
min_length = float('inf')
for l in itertools.permutations(L):
    length = (l[0]*2+l[1]*2)*C[0] + (l[1]*2+l[2]*2)*C[1] + (l[2]*2+l[0]*2)*C[2]
    min_length = min(min_length, length)
print(min_length)
