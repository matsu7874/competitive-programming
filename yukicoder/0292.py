S, t, u = input().split()
t = int(t)
u = int(u)
if t == u:
    S = S[:t] + S[t + 1:]
elif t < u:
    S = S[:t] + S[t + 1:u] + S[u + 1:]
else:
    S = S[:u] + S[u + 1:t] + S[t + 1:]
print(S)
