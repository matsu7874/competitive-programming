def main():
    A,B = [int(x) for x in input().split()]
    path = [[999 for b in range(41)] for a in range(41)]
    for i in range(41):
        path[i][i] = 0
    for command in [-10,-5,-1,1,5,10]:
        for i in range(41):
            if 0 <= i+command <= 40:
                path[i][i+command] = 1
    for k in range(41):
        for i in range(41):
            for j in range(41):
                path[i][j] = min(path[i][j], path[i][k]+path[k][j])
    print(path[A][B])

if __name__ == '__main__':
    main()
