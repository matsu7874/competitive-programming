import math
def f(t, A, B, C):
    return A*t + B*math.sin(C*t*math.pi) - 100
def df(t, A, B, C):
    return A + B*math.cos(C*t*math.pi)*C*math.pi

def main():
    A,B,C = [int(x) for x in input().split()]
    t = 100.0/A
    f_value = f(t,A,B,C)
    while not (-0.000001 < f_value < 0.000001):
        t -= f_value/df(t,A,B,C)
        f_value = f(t,A,B,C)
    print(t)

if __name__ == '__main__':
    main()
