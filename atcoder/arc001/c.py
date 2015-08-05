import itertools
def check(Xs, Ys, Qs):
    X = [q[1] for q in Qs]
    X.extend(Xs)
    Y = [q[0] for q in Qs]
    Y.extend(Ys)
    if len(set([Y[i]-X[i] for i in range(8)])) == 8 and len(set([Y[i]+X[i] for i in range(8)])) == 8:
        return True
    else:
        return False

def main():
    C = [input() for i in range(8)]
    Queens = []
    Queens_X = [i for i in range(8)]
    Queens_Y = [i for i in range(8)]
    for i in range(8):
        for j in range(8):
            if C[i][j] == 'Q':
                Queens.append((i,j))
                if j in Queens_X:
                    Queens_X.remove(j)
                else:
                    print('No Answer')
                    return
                if i in Queens_Y:
                    Queens_Y.remove(i)
                else:
                    print('No Answer')
                    return
    for queens_x in itertools.permutations(Queens_X):
        if check(queens_x, Queens_Y, Queens):
            for i in range(len(queens_x)):
                Queens.append((Queens_Y[i],queens_x[i]))
            cells = [['.' for j in range(8)] for i in range(8)]
            for i,j in Queens:
                cells[i][j] = 'Q'
            for i in range(8):
                print(''.join(cells[i]))
            return
    print('No Answer')

if __name__ == '__main__':
    main()
