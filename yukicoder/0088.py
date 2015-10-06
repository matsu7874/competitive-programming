S = input()
names = ["oda", "yukiko", "oda"]
b = 0
w = 0
for i in range(8):
    B = input()
    b += B.count('b')
    w += B.count('w')
print(names[names.index(S) + (b + w) % 2])
