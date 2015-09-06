import string
import math
N, M = map(int, input().split())
name = input()
kit = input()
number_uppercase = len(string.ascii_uppercase)
name_chars = [0 for i in range(number_uppercase)]
kit_chars = [0 for i in range(number_uppercase)]
for c in string.ascii_uppercase:
    name_chars[ord(c) - ord('A')] = name.count(c)
    kit_chars[ord(c) - ord('A')] = kit.count(c)
need_kit = 0
for i in range(number_uppercase):
    if name_chars[i] > 0 and kit_chars[i] == 0:
        print(-1)
        exit()
    if kit_chars[i] > 0:
        need_kit = max(need_kit, math.ceil(name_chars[i] / kit_chars[i]))
print(need_kit)
