import random
H,W,K,sr,sc = map(int, input().split())

cells = [input() for i in range(H)]
N = int(input())
foods = [map(int, input().split()) for i in range(N)]
ans = []
for i in range(K):
    ans.append(random.choice(['U', 'D', 'L', 'R']))
print(''.join(ans))