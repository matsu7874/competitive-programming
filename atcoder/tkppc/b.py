N = int(input())
max_i = 1
max_a = 0
for i in range(N):
    a = int(input())
    if max_a < a:
        max_i = i+1
        max_a = a
print(max_i)
