# -*- coding: utf-8 -*-
import math,string,itertools,fractions,heapq,collections,re,array,bisect

class CheeseSlicing:
    memo = {}
    def totalArea(self, A, B, C, S):
        if A<C:
            A,C = C,A
        if A<B:
            A,B = B,A
        if B<C:
            B,C = C,B
        if C<S:
            return 0
        if C == S:
            return A*B
        if (A,B,C) in self.memo:
            return self.memo[(A,B,C)]
        self.memo[(A,B,C)] = max([
            self.totalArea(A-S, B, C, S) + self.totalArea(S, B, C, S),
            self.totalArea(A, B-S, C, S) + self.totalArea(A, S, C, S),
            self.totalArea(A, B, C-S, S) + self.totalArea(A, B, S, S),
            A*B,B*C,C*A
        ])
        return self.memo[(A,B,C)]

# CUT begin
# TEST CODE FOR PYTHON {{{
import sys, time, math

def tc_equal(expected, received):
    try:
        _t = type(expected)
        received = _t(received)
        if _t == list or _t == tuple:
            if len(expected) != len(received): return False
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
        return '(%s)' % (','.join( (pretty_str(y) for y in x) ) )
    else:
        return str(x)

def do_test(A, B, C, S, __expected):
    startTime = time.time()
    instance = CheeseSlicing()
    exception = None
    try:
        __result = instance.totalArea(A, B, C, S);
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
        sys.stdout.write("           Expected: " + pretty_str(__expected) + "\n")
        sys.stdout.write("           Received: " + pretty_str(__result) + "\n")
        return 0

def run_tests():
    sys.stdout.write("CheeseSlicing (500 Points)\n\n")

    passed = cases = 0
    case_set = set()
    for arg in sys.argv[1:]:
        case_set.add(int(arg))

    with open("CheeseSlicing.sample", "r") as f:
        while True:
            label = f.readline()
            if not label.startswith("--"): break

            A = int(f.readline().rstrip())
            B = int(f.readline().rstrip())
            C = int(f.readline().rstrip())
            S = int(f.readline().rstrip())
            f.readline()
            __answer = int(f.readline().rstrip())

            cases += 1
            if len(case_set) > 0 and (cases - 1) in case_set: continue
            sys.stdout.write("  Testcase #%d ... " % (cases - 1))
            passed += do_test(A, B, C, S, __answer)

    sys.stdout.write("\nPassed : %d / %d cases\n" % (passed, cases))

    T = time.time() - 1491063353
    PT, TT = (T / 60.0, 75.0)
    points = 500 * (0.3 + (0.7 * TT * TT) / (10.0 * PT * PT + TT * TT))
    sys.stdout.write("Time   : %d minutes %d secs\n" % (int(T/60), T%60))
    sys.stdout.write("Score  : %.2f points\n" % points)

if __name__ == '__main__':
    run_tests()

# }}}
# CUT end
