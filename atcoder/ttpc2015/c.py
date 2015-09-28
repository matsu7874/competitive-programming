S = input()
T = ''
T_start = 0
T_end = 0
step = 1
while True:
    if step == 1:
        S = S[:T_start] + T[:] + S[T_end:]
        if 'oookayama' in S:
            step = 2
        else:
            print(S)
            exit()
    if step == 2:
        len_s = len(S) - 5
        start = 0
        cnt = -2
        max_cnt = -2
        connection = False
        for i in range(len_s):
            if S[i] == 'o':
                if not connection:
                    connection = True
                    start = i
                    cnt = -2
                cnt += 1
            elif S[i:i + 6] == 'kayama':
                connection = False
                if cnt > max_cnt:
                    # T = S[start:i + 6]
                    T_start = start
                    T_end = i + 6
            else:
                connection = False
                cnt = -2
        if max_cnt % 4 == 0:
            T = 'Ookayama'
        elif max_cnt % 4 == 1:
            T = 'okayama'
        elif max_cnt % 4 == 2:
            T = 'okayama'
        elif max_cnt % 4 == 3:
            T = 'okayama'
        step = 1
        #step = 3
    if step == 3:
        if 'oo' in T:
            i = T.index('oo')
            T = T[:i] + 'O' + T[i + 2:]
            step = 4
        else:
            step = 1
    if step == 4:
        if 'OO' in T:
            i = T.index('OO')
            T = T[:i] + 'o' + T[i + 2:]
        step = 3
