N,A,B=map(int, input().split())
if N%(A+B)==0 or N%(A+B)>A:
    print('Bug')
else:
    print('Ant')
