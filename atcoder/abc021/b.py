N = int(input())
a,b = [int(x) for x in input().split()]
K = int(input())
P = [int(x) for x in input().split()]
Test = [a,b]
for p in P:
    if p in Test:
        print('NO')
        exit()
    else:
        Test.append(p)
print('YES')