def pow(x, n):
    ret = 1
    while 0<n:
        if n%2 == 0:
            x = x*x%100000000
            n /= 2
        else:
            ret = ret * x %100000000
            n -= 1
    return ret


def main():
    while True:
        a,x = [int(x) for x in input().split()]
        if a==0 and x==0:
            return
        a = a%100000000
        print(pow(a,x))



if __name__ == '__main__':
    main()
