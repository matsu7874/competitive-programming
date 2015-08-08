S = input()
A = []
m_cnt = 0
p_cnt = 0
for i in range(len(S)):
    s = S[len(S)-1-i]
    if s == 'M':
        A.append(p_cnt)
        m_cnt += 1
    elif s == '+':
        p_cnt += 1
    elif s == '-':
        p_cnt -= 1
A.sort()
print(sum(A[m_cnt//2:]) - sum(A[:m_cnt//2]))
