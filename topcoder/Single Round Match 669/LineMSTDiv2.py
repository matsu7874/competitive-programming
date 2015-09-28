# -*- coding: utf-8 -*-
import math
import string
import itertools
import fractions
import heapq
import collections
import re
import array
import bisect


def minimum_spanning_tree(g, n, r):
    total = 0
    visited = [False] * n
    T = []
    Q = [(-1, r, 0)]
    while Q:
        e = heapq.heappop(Q)
        if visited[e[1]]:
            continue
        T.append(e[:])
        total += e[2]
        visited[e[1]] = True
        for f in range(g[e[1]]):
            if not visited[f]:
                pass


class LineMSTDiv2:

    def count(self, N):
        for costs in itertools.product((1, 2), repeat=N * (N - 1) // 2):
            G = [costs[N*i:N*i+N] for i in range(N)]
            total = 0
            for i in range(N):
                total += minimum_spanning_tree(G,N,i)

        return total

# CUT begin
# TEST CODE FOR PYTHON {{{
import sys
import time
import math


def tc_equal(expected, received):
    try:
        _t = type(expected)
        received = _t(received)
        if _t == list or _t == tuple:
            if len(expected) != len(received):
                return False
            return all(tc_equal(e, r) for (e, r) in zip(expected, received))
        elif _t == float:
            eps = 1e-9
            d = abs(received - expected)
            return not math.isnan(received) and not math.isnan(expected) and d <= eps * max(1.0, abs(expected))
        else:
            return expected == received
    except:
        return False


def pretty_str(x):
    if type(x) == str:
        return '"%s"' % x
    elif type(x) == tuple:
        return '(%s)' % (','.join((pretty_str(y) for y in x)))
    else:
        return str(x)


def do_test(N, __expected):
    startTime = time.time()
    instance = LineMSTDiv2()
    exception = None
    try:
        __result = instance.count(N)
    except:
        import traceback
        exception = traceback.format_exc()
    elapsed = time.time() - startTime   # in sec

    if exception is not None:
        sys.stdout.write("RUNTIME ERROR: \n")
        sys.stdout.write(exception + "\n")
        return 0

    if tc_equal(__expected, __result):
        sys.stdout.write("PASSED! " + ("(%.3f seconds)" % elapsed) + "\n")
        return 1
    else:
        sys.stdout.write("FAILED! " + ("(%.3f seconds)" % elapsed) + "\n")
        sys.stdout.write("           Expected: " +
                         pretty_str(__expected) + "\n")
        sys.stdout.write("           Received: " + pretty_str(__result) + "\n")
        return 0


def run_tests():
    sys.stdout.write("LineMSTDiv2 (1000 Points)\n\n")

    passed = cases = 0
    case_set = set()
    for arg in sys.argv[1:]:
        case_set.add(int(arg))

    with open("LineMSTDiv2.sample", "r") as f:
        while True:
            label = f.readline()
            if not label.startswith("--"):
                break

            N = int(f.readline().rstrip())
            f.readline()
            __answer = int(f.readline().rstrip())

            cases += 1
            if len(case_set) > 0 and (cases - 1) in case_set:
                continue
            sys.stdout.write("  Testcase #%d ... " % (cases - 1))
            passed += do_test(N, __answer)

    sys.stdout.write("\nPassed : %d / %d cases\n" % (passed, cases))

    T = time.time() - 1443438858
    PT, TT = (T / 60.0, 75.0)
    points = 1000 * (0.3 + (0.7 * TT * TT) / (10.0 * PT * PT + TT * TT))
    sys.stdout.write("Time   : %d minutes %d secs\n" % (int(T / 60), T % 60))
    sys.stdout.write("Score  : %.2f points\n" % points)

if __name__ == '__main__':
    run_tests()

# }}}
# CUT end
