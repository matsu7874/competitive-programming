import re
while True:
    s = input()
    if s == '#':
        exit()
    s = re.sub(r'[q|w|e|r|t|a|s|d|f|g|z|x|c|v|b]+', 'q', s)
    s = re.sub(r'[y|u|i|o|p|h|j|k|l|n|m]+', 'p', s)
    print(s.count('qp') + s.count('pq'))
