R,M,K = [int(x) for x in input().split()]
matrix = [[False for j in range(M)] for i in range(R)]
for i in range(K):
    r,c = [int(x)-1 for x in input().split()]
    matrix[r][c] = True
    flg = False
    if r>0 and matrix[r-1][c]:
        if c>0:
            if matrix[r-1][c-1] and matrix[r][c-1]:
                flg = True
        if c<M-1:
            if matrix[r-1][c+1] and matrix[r][c+1]:
                flg = True
    if r<R-1 and matrix[r+1][c]:
        if c>0:
            if matrix[r+1][c-1] and matrix[r][c-1]:
                flg = True
        if c<M-1:
            if matrix[r+1][c+1] and matrix[r][c+1]:
                flg = True
    if flg:
        print(i+1)
        exit()
print(0)