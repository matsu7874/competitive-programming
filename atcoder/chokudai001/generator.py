import random
A = [[random.randint(1,100) for j in range(30)] for i in range(30)]
for i in A:
    print(' '.join([str(j) for j in i]))
