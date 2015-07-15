def main():
    e = [True for i in range(2*123456+1)]
    e[0] = e[1] = False
    i = 2
    while i*i <= 2*123456:
        for j in range(2*i, 2*123456+1, i):
            e[j] = False
        i += 1
    while True:
        n = int(input())
        if n == 0:
            exit()
        print(e[n+1:2*n+1].count(True))

if __name__ == '__main__':
    main()
