n = int(input())
s = []
for i in range(n):
    s.append(int(input()))
for i in range(7):
    print(sum(s[x] for x in range(n) if x%7==i))