"""
Project Euler Problem 14
========================

The following iterative sequence is defined for the set of positive
integers:

n->n/2 (n is even)
n->3n+1 (n is odd)

Using the rule above and starting with 13, we generate the following
sequence:
                  13->40->20->10->5->16->8->4->2->1

It can be seen that this sequence (starting at 13 and finishing at 1)
contains 10 terms. Although it has not been proved yet (Collatz Problem),
it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""
def main():
    limit = 1000000
    chain_length = [0 for i in range(limit)]
    for i in range(1, limit):
        n = i
        cnt = 1
        while n > 1:
            if n >= limit:
                cnt += 1
                if n%2 == 0:
                    n //= 2
                else:
                    cnt += 1
                    n = (n*3+1) // 2
            elif chain_length[n] > 0:
                cnt += chain_length[n]
                n = 1
            else:
                cnt += 1
                if n%2 == 0:
                    n //= 2
                else:
                    cnt += 1
                    n = (n*3+1) // 2
        chain_length[i] = cnt
    print(chain_length.index(max(chain_length)))

if __name__ == '__main__':
    main()
