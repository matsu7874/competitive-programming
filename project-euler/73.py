def gcd(a, b):
    while b > 0:
        a,b = b, a%b
    return a

def main():
    d_max = 12000
    # d_max = 8
    cnt = 0
    # ans = []
    for denominator in range(2,d_max+1):
        numerator = denominator-1
        while denominator < numerator*3:
            if numerator*2 < denominator and gcd(numerator, denominator) == 1:
                cnt += 1
                # ans.append((numerator, denominator))
            numerator -= 1
    print(cnt)
    # print(ans)

if __name__ == '__main__':
    main()
