def main():
    factorial = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]
    ans = 0
    for i in range(1000000):
        if i%10000 == 0:
            print(i/1000000)
        n = i
        terms = []
        while n not in terms:
            terms.append(n)
            a = n
            n = 0
            while a>0:
                n += factorial[a%10]
                a //= 10
        if len(terms) == 60:
            ans += 1
    print(ans)


if __name__ == '__main__':
    main()
