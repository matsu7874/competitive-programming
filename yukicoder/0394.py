a = list(map(int, input().split()))
a.sort()
print('{0:.2f}'.format(sum(a[1:5])/4))