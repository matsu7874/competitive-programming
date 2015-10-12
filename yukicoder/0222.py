S = input()
op_index = 1
while S[op_index] not in '+-':
    op_index += 1
a = int(S[0:op_index])
b = int(S[op_index + 1:])
if S[op_index] == '+':
    b *= -1
print(a + b)
