w, h = map(int, input().split())
if w < h:
    w, h = h, w
mod = 1000000007
nume = 1
for i in range(1, w + h - 1):
    nume = nume * i % mod
deno = 1
for i in range(2, w):
    deno = deno * i % mod
for i in range(2, h):
    deno = deno * i % mod
print(nume * pow(deno, mod - 2, mod) % mod)
