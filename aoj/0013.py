import sys
stack = []
for line in sys.stdin:
    a = int(line)
    if a == 0:
        print(stack.pop())
    else:
        stack.append(a)
