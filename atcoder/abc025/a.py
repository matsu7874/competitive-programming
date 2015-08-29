S = input()
S = ''.join(sorted([s for s in S]))
N = int(input()) - 1
print(S[N // 5] + S[N % 5])
