P, C = map(int, input().split())
p = [2, 3, 5, 7, 11, 13]
c = [4, 6, 8, 9, 10, 12]
e = 0
if P > 0 and C > 0:
    e = (sum(p) / 6)**P * (sum(c) / 6)**C
elif P > 0:
    e = (sum(p) / 6)**P
elif C > 0:
    e = (sum(c) / 6)**C
print(e)
