import random

NUM_TRIAL = 10**4
N = int(input())
HANDS = [0,1,2]

total_round = 0
for _trial in range(NUM_TRIAL):
    n = N
    cnt = 0
    while n>1:
        hands = [random.choice(HANDS) for i in range(n)]
        counts = [hands.count(hand) for hand in HANDS]
        counts.sort()
        if counts[0] == counts[-1] or counts[-1] == n:
            pass
        else:
            if 0 in counts:
                counts.remove(0)
            n = counts[0]
        cnt += 1
#    print(_trial,n,counts)
    total_round += cnt
print(total_round/(NUM_TRIAL))