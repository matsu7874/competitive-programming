N=int(input())
C = input().split()
C.sort()
num = []
op = []
for c in C:
    if c in '+-':
        op.append(c)
    else:
        num.append(int(c))

l = len(op)

nums = []
for i in range(l):
    nums.append(num[i])
t = 0
for i in range(len(num)-len(op)):
    t += num[len(op)+i]*10**i
nums.append(t)
nums.sort()
max_v = nums[-1]
for i in range(l):
    if op[i] == '+':
        max_v += nums[l-i-1]
    else:
        max_v -= nums[l-i-1]

if '-' in op:
    min_v = nums[0]
    for i in range(l):
        if op[i] == '+':
            min_v += nums[i+1]
        else:
            min_v -= nums[i+1]
else:
    nums = [0]*(l+1)
    for i in range(len(num)):
        nums[i%(l+1)] *= 10
        nums[i%(l+1)] += num[i]
    min_v = sum(nums)
print(max_v,min_v)
