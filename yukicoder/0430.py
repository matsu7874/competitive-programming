import collections
text = input()
len_text = len(text)
dic = collections.defaultdict(int)
for i in range(1,11):
    for j in range(len_text-i+1):
        dic[text[j:j+i]] += 1
total = 0
m = int(input())
for i in range(m):
    c = input()
    total += dic[c]
print(total)