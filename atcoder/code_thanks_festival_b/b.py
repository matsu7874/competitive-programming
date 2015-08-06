a = int(input())
b = int(input())
c = int(input())
print(max(max(a+b, a*b)+c, max(a+b, a*b)*c))
