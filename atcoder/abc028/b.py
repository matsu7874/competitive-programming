cnt = [0 for i in range(6)]
S = input()
for c in S:
    cnt[ord(c) - ord('A')] += 1
print(*cnt)
