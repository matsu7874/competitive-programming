def nth_cell(t):
    return t//100 * 12 + t%100//5

def round_before(t):
    if t%5 != 0:
        t -= (t%5)
    return t

def round_after(t):
    if t%5 != 0:
        t += 5-(t%5)
    return t

N = int(input())
rain = [0 for i in range(12*24+2)]
for _ in range(N):
    (s, e) = map(int, input().split('-'))
    for i in range(nth_cell(round_before(s)), nth_cell(round_after(e))):
        rain[i] = 1
buff = ""
for i in range(len(rain)):
    if (i==0 or rain[i-1]==0) and rain[i]==1:
        h_s = i//12
        if h_s<10:
            buff += '0'
        buff += str(h_s)
        m_s = i%12*5
        if m_s<10:
            buff += '0'
        buff += str(m_s)
        buff += '-'
    if rain[i]==1 and rain[i+1]==0:
        h_e = (i+1)//12
        if h_e<10:
            buff += '0'
        buff += str(h_e)
        m_e = (i+1)%12*5
        if m_e<10:
            buff += '0'
        buff += str(m_e)
        print(buff)
        buff = ''