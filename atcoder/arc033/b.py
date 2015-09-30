Na, Nb = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
A.sort()
B.sort()

AandB = 0
cur_a = 0
cur_b = 0
while cur_a < Na and cur_b < Nb:
    if A[cur_a] < B[cur_b]:
        cur_a += 1
    elif A[cur_a] == B[cur_b]:
        AandB += 1
        cur_a += 1
        cur_b += 1
    else:
        cur_b += 1
        
AorB = Na + Nb - AandB
print(AandB/AorB)
