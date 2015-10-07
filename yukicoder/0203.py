C = input()
D = input()
C = C + D
for i in range(14, 0, -1):
    if 'o' * i in C:
        print(i)
        exit()
print(0)
