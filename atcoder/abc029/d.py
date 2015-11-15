N = int(input())
total = 0
for i in range(9):
    i_th_digit = N % (10**(i + 1)) // (10**i)
    total += N // (10**(i + 1)) * (10**i)
    if i_th_digit == 0:
        pass
    elif i_th_digit == 1:
        total += N % (10**(i + 1)) % (10**i) + 1
    else:
        total += 10**i

print(total)
