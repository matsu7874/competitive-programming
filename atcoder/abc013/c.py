N, H = map(int, input().split())
A, B, C, D, E = map(int, input().split())
if B * C - E * (A - C) <= D * A:
    dt = (N * E - H) // (D + E)
    min_cost = (dt + 1) * C
    for d in range(dt - A, dt + 1):
        b = (N * E - H - (D + E) * d) // B + E + 1
        if B * b + D * d + H > (N - b - d) * E:
            min_cost = min(min_cost, A * b + C * d)
    print(min_cost)
else:
    pass
