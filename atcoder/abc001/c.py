(Deg, Dis) = map(int, input().split())
Deg = Deg * 10
Dis = Dis / 60
DIS_W = [0, 0.25, 1.55, 3.35, 5.45, 7.95, 10.75,
         13.85, 17.15, 20.75, 24.45, 28.45, 32.65]
DEG_DIR = ['N', 'NNE', 'NE', 'ENE', 'E', 'ESE', 'SE', 'SSE',
           'S', 'SSW', 'SW', 'WSW', 'W', 'WNW', 'NW', 'NNW', 'N']
for i in range(len(DIS_W)):
    if Dis >= DIS_W[i]:
        W = i

for i in range(len(DEG_DIR)):
    if Deg >= (3375 - 1125) * i - 1125:
        Dir = DEG_DIR[i]

if W == 0:
    Dir = 'C'

print(Dir, W)
