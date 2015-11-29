import sys
answer = ['0']*10

print('0'*10)
sys.stdout.flush()
zero, lock = input().split()
zero = int(zero)
if zero == 10:
    exit()

for i in range(10):
    for j in range(1,10):
        print('0'*i+str(j)+'0'*(9-i))
        sys.stdout.flush()
        x, lock = input().split()
        if int(x) == 10:
            exit()
        if int(x) > zero:
            answer[i] = str(j)
            break
        elif int(x) < zero:
            break

print(''.join(answer))
sys.stdout.flush()
x, lock = input().split()
exit()
