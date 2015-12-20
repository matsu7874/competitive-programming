N = int(input())
n = N % 9
if n == 0:
    n = 9
m = (N-1)//9 + 1
print(str(n) * m)
