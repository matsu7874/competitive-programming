s = input()
if len(s)==2:
    if s[0]==s[1]:
        print(1,2)
    else:
        print(-1,-1)
    exit()
for i in range(len(s)-1):
    if s[i] == s[i+1]:
        print(i+1,i+2)
        exit()
for i in range(len(s)-2):
    if s[i] == s[i+2]:
        print(i+1,i+3)
        exit()
print(-1,-1)
