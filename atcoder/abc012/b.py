N = int(input())
h = N // (60 * 60)
m = N % (60 * 60) // 60
s = N % 60
print("{0:02d}:{1:02d}:{2:02d}".format(h, m, s))
