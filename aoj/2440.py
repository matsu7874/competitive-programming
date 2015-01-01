def main():
    N = int(input())
    IDs = []
    for _ in range(N):
        IDs.append(input())
    locked = True
    M = int(input())
    for _ in range(M):
        t = input()
        if t in IDs:
            if locked:
                print('Opened by', t)
                locked = False
            else:
                print('Closed by', t)
                locked = True
        else:
            print('Unknown', t)

if __name__ == '__main__':
    main()