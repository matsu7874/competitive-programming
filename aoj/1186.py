import itertools
S=[]
for i in range(1,150):
    for j in range(1,i):
        S.append((i*i+j*j,j,i))
S.sort()
while True:
    h,w=map(int, input().split())
    if h==0 and w==0:
        exit()
    s = S[S.index((w*w+h*h,h,w))+1]
    print(s[1],s[2])
