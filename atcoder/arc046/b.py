n = int(input())
a, b = map(int, input().split())
winner = 'Takahashi'
if n > a:
    if a == b and n % (a + 1) == 0:
        winner = 'Aoki'
    if a != b and b > a:
        winner = 'Aoki'
print(winner)
