A, B = map(int, input().split())
cnt = 0
cnt += B // 4 - (A - 1) // 4
cnt -= B // 100 - (A - 1) // 100
cnt += B // 400 - (A - 1) // 400
print(cnt)
