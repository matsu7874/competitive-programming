a, b = map(int, input().split())
diff = b - a
if diff > 0:
    print('+' + str(diff))
else:
    print(diff)
