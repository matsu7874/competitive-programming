p = 0
for i in range(3):
    (s, e) = [int(x) for x in input().split()]
    p += (s*e)/10
print(int(p))
