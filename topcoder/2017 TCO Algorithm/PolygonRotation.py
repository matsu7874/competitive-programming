# -*- coding: utf-8 -*-
import math,string,itertools,fractions,heapq,collections,re,array,bisect

class PolygonRotation:
    def get_gxS(self, points):
        n = len(points)
        S = 0
        gx = 0
        for i in range(1, n-1):
            Si = (points[i+1][0] - points[i][0])*(points[i+1][1] + points[i][1])/2
            S += Si
            gx += (points[i+1][1] + points[i][1])/4 * Si
        Si = (points[1][0] - points[0][0])*(points[1][1] + points[0][1])/2
        S += Si
        gx += (points[1][1])/3*Si
        Si = (points[n-1][0] - points[n-2][0])*(points[n-1][1] + points[n-2][1])/2
        S += Si
        gx += (points[n-1][1])/3*Si
        return gx
    def get_cross(a, b, c, d):
        S1 = ((b[1]-a[1])*(c[0]-a[0])-(b[0]-a[0])*(c[1]-a[1]))/2
        S1 = ((b[1]-a[1])*(a[0]-d[0])-(b[0]-a[0])*(a[1]-d[1]))/2
        x = c[1] + (d[1]-c[1])*S1/(S1+S2)
        y = c[0] + (d[0]-c[0])*S2/(S1+S2)
    def getVolume(self, x, y):
        import math
        n = len(y)
        points = [(y[i], x[i]) for i in range(n)]
        pos = []
        neg = []
        for i in range(1, n-1):
            if points[i][1] < 0:
                neg.append((points[i][0], -points[i][1]))
            elif points[i][1]>0:
                pos.append(points[i][:])

                
        points = [points[0][:]]
        pi = 0
        ni = 0
        ppy = npy = points[0][0]
        ppx = npx = 0
        while pi < len(pos) and ni < len(neg):
            if pos[pi][0] < neg[ni][0]:
                if 



        return self.get_gxS(points) * 2 * math.pi

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

def do_test(x, y, __expected):
    startTime = time.time()
    instance = PolygonRotation()
    exception = None
    try:
        __result = instance.getVolume(x, y);
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
    sys.stdout.write("PolygonRotation (1000 Points)\n\n")

    passed = cases = 0
    case_set = set()
    for arg in sys.argv[1:]:
        case_set.add(int(arg))

    with open("PolygonRotation.sample", "r") as f:
        while True:
            label = f.readline()
            if not label.startswith("--"): break

            x = []
            for i in range(0, int(f.readline())):
                x.append(int(f.readline().rstrip()))
            x = tuple(x)
            y = []
            for i in range(0, int(f.readline())):
                y.append(int(f.readline().rstrip()))
            y = tuple(y)
            f.readline()
            __answer = float(f.readline().rstrip())

            cases += 1
            if len(case_set) > 0 and (cases - 1) in case_set: continue
            sys.stdout.write("  Testcase #%d ... " % (cases - 1))
            passed += do_test(x, y, __answer)

    sys.stdout.write("\nPassed : %d / %d cases\n" % (passed, cases))

    T = time.time() - 1491064130
    PT, TT = (T / 60.0, 75.0)
    points = 1000 * (0.3 + (0.7 * TT * TT) / (10.0 * PT * PT + TT * TT))
    sys.stdout.write("Time   : %d minutes %d secs\n" % (int(T/60), T%60))
    sys.stdout.write("Score  : %.2f points\n" % points)

if __name__ == '__main__':
    run_tests()

# }}}
# CUT end
