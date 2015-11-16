import itertools
for guardians in itertools.combinations(range(100), 4):
    directions = [(-2, -2), (-2, 0), (-2, 2), (-1, -1), (-1, 0), (-1, 1),
                  (0, -2), (0, -1), (0, 0), (0, 1), (0, 2),
                  (1, -1), (1, 0), (1, 1), (2, -2), (2, 0), (2, 2)]
    table = ['.' for i in range(100)]
    for g in guardians:
        gy = g//10
        gx = g%10
        for dy,dx in directions:
            if 0<=gy+dy<10 and 0<=gx+dx<10:
                table[g+dy*10+dx] = 'x'

    path = [0 for i in range(100)]
    for y in range(10):
        path[9 + 10 * y] = 1

    for x in range(8, -1, -1):
        for y in range(1, 10):
            p = 10 * y + x
            if table[p] == '.' and table[p - 9] == '.':
                path[p] += path[p - 9]
        for y in range(10):
            p = 10 * y + x
            if table[p] == '.' and table[p + 1] == '.':
                path[p] += path[p + 1]
        for y in range(9):
            p = 10 * y + x
            if table[p] == '.' and table[p + 11] == '.':
                path[p] += path[p + 11]

    if sum(path[10 * y] for y in range(10)) == 1:
        table = ['.' for i in range(100)]
        for g in guardians:
            table[g] = 'C'
        for y in range(10):
            print(''.join(table[10 * y:10 * (y + 1)]))
        exit()
