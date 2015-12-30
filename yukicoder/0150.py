def Hamming_distance(a, b):
    dist = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            dist += 1
    return dist

T = int(input())
for _ in range(T):
    S = input()
    min_dist = float('inf')
    for i in range(len(S) - len('problem') - len('good') + 1):
        hd_good = Hamming_distance('good', S[i:i + len('good')])
        if hd_good >= min_dist:
            continue
        for j in range(i + len('good'), len(S) - len('problem') + 1):
            hd_problem = Hamming_distance('problem', S[j:j + len('problem')])
            min_dist = min(min_dist, hd_good + hd_problem)
    print(min_dist)
