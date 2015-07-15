def gcd(a, b):
    while b > 0:
        a,b = b, a%b
    return a

def main():
    d_max = 1000000
    cnt = 0
    for denominator in range(1,d_max+1):
        for numerator in range(1, denominator):
            if gcd(numerator, denominator) == 1:
                cnt += 1
    print(cnt)

if __name__ == '__main__':
    main()
