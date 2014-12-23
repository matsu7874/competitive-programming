w = [[''],['.',',','!','?',' '], ['a','b','c'], ['d','e','f'], ['g','h','i'], ['j','k','l'], ['m','n','o'], ['p','q','r','s'], ['t','u','v'], ['w','x','y','z']]
n = int(input())
for _ in range(n):
    buff = ''
    s = input()
    push = 0
    times = 0
    for c in s:
        if int(c) == 0:
            buff += w[push][times%len(w[push])]
        if int(c) == push:
            times += 1
        else:
            push = int(c)
            times = 0
    print(buff)