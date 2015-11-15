import string


def maxBy(f, x, y):
    if f(x) > f(y):
        return x
    else:
        return y

table = {("", ""): ""}


def lcs(xs, ys):
    if (xs, ys) in table:
        return table[(xs, ys)]

    ret = ""
    if xs == "" or ys == "":
        ret = ""
    elif xs[-1] == ys[-1]:
        ret = lcs(xs[:-1], ys[:-1]) + xs[-1]
    else:
        ret = maxBy(len,
                    lcs(xs[:-1], ys),
                    lcs(xs, ys[:-1]))
    table[(xs, ys)] = ret
    return ret

N = int(input())
S = input()
max_len = 0
for i in range(1, N):
    a = S[:i]
    b = S[i:]
    max_len = max(max_len, len(lcs(a, b)))
print(N - max_len * 2)
