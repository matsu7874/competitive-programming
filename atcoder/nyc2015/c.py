s = input()
t = input()
len_t = len(t)
len_s = len(s)

if s[0] != t[0]:
    print('No')
    exit()

for i in range(len_t):
    if len_s<=i or s[i]!=t[i]:
        if t[i-1] == t[i]:
            for j in range(2,i+1):
                if i>=j and s[i-j]!=t[i]:
                    s = s[:i]+t[i]+s[i:]
                    len_s += 1
                    break
            else:
                print('No')
                exit()
        else:
            s = s[:i]+t[i]+s[i:]
            len_s += 1
if s != t:
    print('No')
else:
    print('Yes')
