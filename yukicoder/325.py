N,PA,PB = [float(x) for x in input().split()]
N = int(N)
A = [int(x) for x in input().split()]
A.sort()
B = [int(x) for x in input().split()]
B.sort()
P_A_win = 0.0
def calc(Sa,Sb,Ha,Hb,P):
    if len(Ha)<=1:
        if Ha[0]>Hb[0]:
            Sa += Ha[0]+Hb[0]
        else:
            Sb += Ha[0]+Hb[0]
        if Sa>Sb:
            print(P)
            return P
        else:
            return 0
    else:
        PP = 0.0
        for ha in Ha:
            for hb in Hb:
                sa = sb = 0
                if ha>hb:
                    sa = ha+hb
                else:
                    sb = ha+hb
                if ha == Ha[0]:
                    pa = PA
                else:
                    pa = (1-PA)/(len(Ha)-1)
                if hb == Hb[0]:
                    pb = PB
                else:
                    pb = (1-PB)/(len(Hb)-1)

                PP + calc(Sa+sa,Sb+sb,[x for x in Ha if x != ha],[x for x in Hb if x != hb],P*pa*pb)
        return PP
P_A_win = calc(0,0,A,B,1)
print(P_A_win)