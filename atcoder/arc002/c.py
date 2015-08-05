import itertools

def main():
    N = int(input())
    C = input()
    min_len = 1000
    for R in itertools.product('ABXY', repeat=2):
        C_R = C.replace(''.join(R),'R')
        for L in itertools.product('ABXY', repeat=2):
            C_RL = C_R.replace(''.join(L),'L')
            # print(R,L,len(C_RL))
            # if min_len > len(C_RL):
            #     print(R,L,len(C_RL))
            min_len = min(min_len, len(C_RL))
    print(min_len)

if __name__ == '__main__':
    main()
