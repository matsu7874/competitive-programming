# A, B = [int(x) for x in input().split()]


def count(n):
    if n == 0:
        return 1
    total = 0
    num_digits = 0

    while 10**num_digits <= n:
        num_digits += 1
    top_digit = n % 10**num_digits // 10**(num_digits - 1)

    if top_digit == 9:
        total =  8 ** num_digits
    elif top_digit > 4:
        total = (top_digit-1) * 8 ** (num_digits - 1)
    elif top_digit == 4:
        total = 3 * 8 ** (num_digits - 1)
    else:
        total = top_digit * 8 ** (num_digits - 1)

    print(total)

    if top_digit ==9 or top_digit ==4:
        total += 1
    else:
        pro = 1
        for i in range(num_digits-1):
            i_th_digit = (n % 10**(i+1) // 10**i)
            if i_th_digit == 9:
                pro *= 8
            elif i_th_digit >= 4:
                pro *= i_th_digit
            else:
                pro *= i_th_digit+1
        total += pro
    print(n, num_digits, top_digit, total)
    return total

# print(B - A + 1 - count(B) + count(A - 1))
for i in range(12):
    count(i)
