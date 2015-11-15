def main():
    p = [True for i in range(100000)]
    p[0] = False
    p[1] = False
    i = 2
    while i*i<=100000:
        if p[i]:
            for j in range(i*i, 100000, i):
                p[j] = False
        i += 1
    for _ in range(10):
        n = int(input())
        print(p[:n].count(True))

if __name__ == '__main__':
    main()
