def main():
    N = int(input())
    S = [input() for i in range(N)]
    M = int(input())
    P = [input().split() for i in range(M)]
    C = input()
    D = input()
    path = [[] for i in range(N)]
