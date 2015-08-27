n = int(input())
s = input()
gpa = 0
for c in s:
    if c == 'A':
        gpa += 4
    elif c == 'B':
        gpa += 3
    elif c == 'C':
        gpa += 2
    elif c == 'D':
        gpa += 1
print(gpa / n)
