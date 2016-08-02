a,b,k,l=map(int, input().split())
print((k//l)*b + min(b,(k-k//l*l)*a))