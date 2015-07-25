def main():
    N,M = [int(x) for x in input().split()]
    T = {i+1:-i-1 for i in range(N)}
    for i in range(M):
        t = int(input())
        T[t] = i
    for k, v in sorted(T.items(), key=lambda x:x[1])[::-1]:
        print(k)

if __name__ == '__main__':
    main()
