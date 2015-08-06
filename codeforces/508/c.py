M,T,R = [int(x) for x in input().split()]
W = [int(x) for x in input().split()]
W.sort()
if T<R:
    print(-1)
    exit()
candle_cnt = 0
candles_num = [0 for i in range(601)]
for w in W:
    for i in range(R):
        if candles_num[w]<R:
            for j in range(w-i,w-i+T):
                candles_num[j] += 1
            candle_cnt += 1
        else:
            break
print(candle_cnt)