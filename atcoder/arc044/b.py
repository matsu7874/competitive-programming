def get_degree(lst):
    degree = {}
    for i in lst:
        if i not in degree:
            degree.update({i: 1})
        else:
            degree[i] += 1
    return degree

N = int(input())
A = list(map(int, input().split()))
A.sort()
degree = get_degree(A)
t = 0
for i in range(0, max(A) + 1):
    if degree[i] == 0:
        print(0)
        exit()
    else:
        t +=
