s = input()
l = len(s)
cnt = 0
pre2 = False
pre5 = False
cnt25 = 0
for i in range(l):
    if pre2 and s[i] == '5':
        cnt25 += 1
    elif pre5 and s[i] == '2':
        pass
    else:
        cnt += (cnt25*(cnt25+1))//2
        cnt25 = 0 

    if s[i] == '2':
        pre2 = True
    else:
        pre2 = False

    if s[i] == '5':
        pre5 = True
    else:
        pre5 = False
cnt += (cnt25*(cnt25+1)//2)
print(cnt)
