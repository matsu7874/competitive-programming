A = [100, 100, 200]
for i in range(3, 20):
    A.append(A[i-1] + A[i-2] + A[i-3])
print(A[19])
