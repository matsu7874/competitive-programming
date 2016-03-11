a,b=map(int, input().split())
diff = b-a
if a<0<b:
    diff -= 1
print(diff)
