N=int(input())
for i in range(101):
    if i*i>=N:
        print(i*i-N)
        exit()
