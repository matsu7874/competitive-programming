X,Y=map(int, input().split())
x,y=map(int, input().split())
if abs(X)==abs(Y) and abs(x)<abs(X) and abs(x)==abs(y):
    print(abs(X)+1)
else:
    print(max(abs(X), abs(Y)))
