def main():
    N = int(input())
    C = input()
    cnt = [C.count(chr(i+ord('1'))) for i in range(4)]
    print(max(cnt), min(cnt))
    
if __name__ == '__main__':
    main()
