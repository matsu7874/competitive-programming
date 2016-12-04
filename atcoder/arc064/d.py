s = input()
def solve(s):
    head = s[0]
    tail = s[-1]
    len_s = len(s)
    res = len_s -2
    if head == tail:
        res -= 1
    for c in s[1:-1]:
        if c != head and c != tail:
            return res%2 == 1 
    return False
print('First' if solve(s) else 'Second')

memo = {}
def state(s):
    if s in memo:
        return memo[s]
    len_s = len(s)
    if len_s == 3:
        if s[0] == s[-1]:
            memo[s] = False
            return False
        memo[s] = True
        return True
    for i in range(1, len_s-1):
        if s[i-1] == s[i+1]:
            continue
        next_state = s[:i] + s[i+1:]
        if state(next_state) == False:
            memo[s] = True
            return True
    memo[s] = False
    return False


        
# for s in ['ab','aba','abc','abcd', 'abcde','abcabcabc', 'asagwegaafdfdg']:
#     print(state(s) == solve(s), state(s), solve(s))

