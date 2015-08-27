W = input()
answer_str = ''
for w in W:
    if w not in ['a', 'i', 'u', 'e', 'o']:
        answer_str += w
print(answer_str)
