# -*- coding: utf-8 -*-
import math,string,itertools,fractions,heapq,collections,re,array,bisect

class Drbalance:
    def get_balance(self,A):
        cnt=0
        for a in A:
            if a>0:
                cnt+=1
        return cnt
    def lesscng(self, s, k):
        L=len(s)
        B=[0]*(L)
        for i in range(L):
            if s[i]=='-':
                B[i]+=1
            else:
                B[i]-= 1
        for i in range(L-1):
            B[i+1]+=B[i]
        cnt=0
        while True:
            g = self.get_balance(B)
            if g==k:
                return cnt
            elif g>k:
                cnt+=1
                n=0
                for b in B:
                    if b==1 or b==2:
                        n+=1
                if g-k<=n:
                    return cnt
                for i in range(L):
                    B[i]-=2
            else:
                cnt+=1
                n=0
                for b in B:
                    if b==0 or b==1:
                        n+=1
                if k-g<=n:
                    return cnt
                for i in range(L):
                    B[i]+=2
        return 0

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

def do_test(s, k, __expected):
    startTime = time.time()
    instance = Drbalance()
    exception = None
    try:
        __result = instance.lesscng(s, k);
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
    sys.stdout.write("Drbalance (450 Points)\n\n")

    passed = cases = 0
    case_set = set()
    for arg in sys.argv[1:]:
        case_set.add(int(arg))

    with open("Drbalance.sample", "r") as f:
        while True:
            label = f.readline()
            if not label.startswith("--"): break

            s = f.readline().rstrip()
            k = int(f.readline().rstrip())
            f.readline()
            __answer = int(f.readline().rstrip())

            cases += 1
            if len(case_set) > 0 and (cases - 1) in case_set: continue
            sys.stdout.write("  Testcase #%d ... " % (cases - 1))
            passed += do_test(s, k, __answer)

    sys.stdout.write("\nPassed : %d / %d cases\n" % (passed, cases))

    T = time.time() - 1444493128
    PT, TT = (T / 60.0, 75.0)
    points = 450 * (0.3 + (0.7 * TT * TT) / (10.0 * PT * PT + TT * TT))
    sys.stdout.write("Time   : %d minutes %d secs\n" % (int(T/60), T%60))
    sys.stdout.write("Score  : %.2f points\n" % points)

if __name__ == '__main__':
    run_tests()

# }}}
# CUT end
