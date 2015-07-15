while True:
    flg = True
    S = input()
    if S == '.':
        exit()
    brackets = []
    for c in S:
        if c == '[':
            brackets.append('[')
        elif c == ']':
            if len(brackets) == 0:
                flg = False
                break
            if brackets.pop() != '[':
                flg = False
                break
        elif c == '(':
            brackets.append('(')
        elif c == ')':
            if len(brackets) == 0:
                flg = False
                break
            if brackets.pop() != '(':
                flg = False
                break
        else:
            pass
    if len(brackets) > 0:
        flg = False
    if flg:
        print('yes')
    else:
        print('no')
