N = int(input())
S = input()
T = 'b'
step = 0
while len(T) < N:
    step += 1
    if step % 3 == 0:
        T = 'b' + T + 'b'
    elif step % 3 == 1:
        T = 'a' + T + 'c'
    elif step % 3 == 2:
        T = 'c' + T + 'a'
if S == T:
    print(step)
else:
    print(-1)
