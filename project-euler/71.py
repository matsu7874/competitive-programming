def gcd(a, b):
    while b > 0:
        a,b = b, a%b
    return a

def main():
    d_max = 1000000
    best_numerator = 2
    best_denominator = 5
    for denominator in range(8,d_max+1):
        numerator = denominator*3//7
        while best_numerator/best_denominator < numerator/denominator:
            if numerator/denominator < 3/7 and gcd(numerator, denominator) == 1:
                # print(numerator,denominator,numerator/denominator)
                best_numerator = numerator
                best_denominator = denominator
                break
            numerator -= 1
    print(best_numerator)
    print(best_denominator)
    print(best_numerator / best_denominator)


if __name__ == '__main__':
    main()
