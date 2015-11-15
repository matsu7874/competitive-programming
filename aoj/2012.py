def main():
    while True:
        e = int(input())
        if e==0:
            return
        m = e
        z = int(e**(1/3))
        while z >= 0:
            y = int(int(e-z**3)**(1/2))
            while y >= 0:
                x = e - z**3 - y**2
                m = min(m, x+y+z)
                y -= 1
            z -= 1
        print(m)

if __name__ == '__main__':
    main()
