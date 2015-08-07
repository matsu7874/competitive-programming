"""
Project Euler Problem 26
========================

A unit fraction contains 1 in the numerator. The decimal representation of
the unit fractions with denominators 2 to 10 are given:

   1/2  =  0.5
   1/3  =  0.(3)
   1/4  =  0.25
   1/5  =  0.2
   1/6  =  0.1(6)
   1/7  =  0.(142857)
   1/8  =  0.125
   1/9  =  0.(1)
  1/10  =  0.1

Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can
be seen that ^1/[7] has a 6-digit recurring cycle.

Find the value of d < 1000 for which ^1/[d] contains the longest recurring
cycle in its decimal fraction part.
"""


def main():
    max_d = 0
    max_l = 0
    for d in range(2,1000):
        N = [1]
        A = []
        i = 0
        have_cycle = False
        cycle_length = 0
        while N[i]>0 and not have_cycle:
            for j in range(i):
                if N[i] == N[j]:
                    have_cycle = True
                    cycle_length = i-j
                    break
            if not have_cycle:
                A.append(N[i]//d)
                N.append(N[i]%d*10)
                i += 1
        if max_l < cycle_length:
            max_d = d
            max_l = cycle_length
    print(max_d)




if __name__ == '__main__':
    main()
