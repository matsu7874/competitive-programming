S = input()
for s in S:
    if s.islower():
        print(s.upper(), end="")
    else:
        print(s.lower(), end="")
print()
