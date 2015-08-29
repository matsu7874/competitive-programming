score = [int(input()) for i in range(3)]
s = sorted(score)[::-1]
for i in range(3):
    print(s.index(score[i]) + 1)
