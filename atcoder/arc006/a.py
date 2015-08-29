E = input().split()
B = input()
L = input().split()
cnt = 0
for l in L:
    if l in E:
        cnt += 1
prize = 0
if cnt == 6:
    prize = 1
elif cnt == 5 and B in L:
    prize = 2
elif cnt == 5:
    prize = 3
elif cnt == 4:
    prize = 4
elif cnt == 3:
    prize = 5
print(prize)
