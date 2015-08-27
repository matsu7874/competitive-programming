N = int(input())

cards = [1, 2, 3, 4, 5, 6]
N = N % 30
for i in range(N):
    cards[(i % 5)], cards[(i % 5) + 1] = cards[(i % 5) + 1], cards[(i % 5)]
text = "".join(map(str, cards))
print(text)
