(n, k) = [int(x) for x in input().split()]
a = [int(x) for x in input().split()]
s = 0
ans = []
ans_ = []
b = sorted(a)

for B in b:
    if s+B <= k:
        s += B
        ans_.append(B)
    else:
        break
len_ans_ = len(ans_)
if len_ans_ == 0:
    print(0)
    exit()
ans.append(a.index(ans_[0])+1)
for i in range(1,len_ans_):
    if ans_[i] == ans_[i-1]:
        ans.append(a[ans[-1]:].index(ans_[i]) + ans[-1] + 1)
    else:
        ans.append(a.index(ans_[i])+1)
ans.sort()

print(len(ans))
if len(ans) > 0:
    print(*ans)
