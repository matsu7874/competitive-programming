N = int(input())
A = [int(x) for x in input().split()]
B = [int(x) for x in input().split()]
def calc(Sa,Sb,Ha,Hb,P):
    if len(Ha)<=1:
        if Ha[0]>Hb[0]:
            Sa += 1
        else:
            Sb += 1
        if Sa>Sb:
            return P
        else:
            return 0
    else:
        PP = 0.0
        for ha in Ha:
            for hb in Hb:
                sa = sb = 0
                if ha>hb:
                    sa = 1
                else:
                    sb = 1
                pa = 1/len(Ha)
                pb = 1/len(Hb)
                PP += calc(Sa+sa,Sb+sb,[x for x in Ha if x != ha],[x for x in Hb if x != hb],P*pa*pb)
        return PP
P_A_win = calc(0,0,A,B,1)
print(P_A_win)