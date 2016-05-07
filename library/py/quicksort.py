def quicksort(A):
    if len(A) < 1:
        return A
    pivot = A[0]
    left = []
    right = []
    for x in range(1, len(A)):
        if A[x] <= pivot:
            left.append(A[x])
        else:
            right.append(A[x])
    left = quicksort(left)
    right = quicksort(right)
    foo = [pivot]
    return left + foo + right
