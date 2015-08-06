Aw,Ab = [int(x) for x in input().split()]
Bw,Bb = [int(x) for x in input().split()]
C,D = [int(x) for x in input().split()]
Aw -= max(C-Ab, 0)
Bw += max(C-Ab, 0)
Aw += min(Bw,D)
print(Aw)