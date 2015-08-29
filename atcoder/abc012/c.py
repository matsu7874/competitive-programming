N = int(input())
correct_sum = 0
for i in range(1, 10):
    for j in range(1, 10):
        correct_sum += i * j
unadded_product = correct_sum - N
for i in range(1, 10):
    for j in range(1, 10):
        if i * j == unadded_product:
            print(i, 'x', j)
