while True:
    (N, Q) = [int(x) for x in input().split()]
    if N==0 and Q==0:
        exit()
    Date = [0]*100
    meeting_day = 0
    member_num = 0
    for i in range(N):
        M = [int(x) for x in input().split()]
        for j in range(1, M[0]+1):
            Date[M[j]-1] += 1
    for i in range(100):
        if Date[i] >= Q and Date[i]>member_num:
            meeting_day = i+1
            member_num = Date[i]
    print(meeting_day)
