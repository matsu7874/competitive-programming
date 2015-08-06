N = int(input())%10
M = int(input())
if M == 0:
    print(1)
    exit()
loop = [N]
n = (N**2)%10
cnt = 1
while n not in loop:
    cnt += 1
    loop.append(n)
    n = (n*N)%10
ans = loop[M%len(loop)-1]
print(ans)