import string
S = input()
N = len(S)
K = int(input())
for i in range(N//K):
    Ti = [S[K*(i+1)-j-1] for j in range(K)]
    # print(Ti,end=" ")
    for c in string.ascii_uppercase:
        cnt = Ti.count(c)
        for j in range(cnt-1):
            Ti.remove(c)
    print(''.join(Ti[::-1]))
