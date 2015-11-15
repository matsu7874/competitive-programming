import random

for i in range(50):
    f = open('random_' + ('0' + str(i))[-2:] + '.in', 'w')
    num = random.randint(5,30)
    A = [1 for _ in range(num)]
    margin = 100 - num *1
    while margin > 0:
        A[random.randint(0, num - 1)] += 1
        margin -= 1
    A.sort()
    A.reverse()
    f.write(str(num) + '\n')
    for j in range(num):
        f.write(str(A[j]) + '\n')
    f.close()
