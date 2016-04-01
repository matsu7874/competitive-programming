import sys
import random
import itertools

popu = [[j for j in range(10)] for i in range(4)]
ans = []
his = []
a = [0, 1, 2, 3]
while True:
    print(*a)
    sys.stdout.flush()
    x, y = map(int, input().split())

    for i in range(4):
        for j in range(x):
            popu[i].append(a[i])
        for j in range(4):
            if j == i:
                continue
            for k in range(y):
                popu[j].append(a[i])

    if x == 4:
        exit()
    if x + y == 4:
        ans = a[:]
        break

    if x == 0:
        for i in range(4):
            while a[i] in popu[i]:
                popu[i].remove(a[i])
    if y == 0:
        for i in range(4):
            for j in range(4):
                if j == i:
                    continue
                while a[i] in popu[j]:
                    popu[j].remove(a[i])
    his.append(a[:])
    a = [random.choice(popu[i]) for i in range(4)]
    while any([a.count(i) > 1 for i in range(10)]) or a in his:
        a = [random.choice(popu[i]) for i in range(4)]


for a in itertools.permutations(ans):
    print(*a)
    sys.stdout.flush()
    x, y = map(int, input().split())
    if x == 4:
        exit()
