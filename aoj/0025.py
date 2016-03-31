import sys
inputs = []
for line in sys.stdin:
    inputs.append(line)

n = len(inputs)
for _ in range(n // 2):
    a = list(map(int, inputs[_ * 2].split()))
    b = list(map(int, inputs[_ * 2 + 1].split()))
    hit = 0
    blow = 0
    for i in range(4):
        if b[i] == a[i]:
            hit += 1
        elif b[i] in a:
            blow += 1
    print(hit, blow)
