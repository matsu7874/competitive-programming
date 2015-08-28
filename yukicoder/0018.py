S = input()
T = []
for i in range(len(S)):
    T.append(chr(ord('A')+(ord(S[i])-ord('A')-(i+1))%(ord('Z')-ord('A')+1)))
print(''.join(T))
