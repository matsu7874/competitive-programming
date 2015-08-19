import queue

def bit_count(n):
    return bin(n).count('1')

N = int(input())
visited = [False for i in range(N+1)]
q = queue.Queue()
q.put((1,1))
while not q.empty():
    t = q.get()
    if visited[t[0]]:
        continue
    visited[t[0]] = True
    if t[0] == N:
        print(t[1])
        exit()
    bc = bit_count(t[0])
    if t[0]-bc > 0 and not visited[t[0]-bc]:
        q.put((t[0]-bc,t[1]+1))
    if t[0]+bc <= N and not visited[t[0]+bc]:
        q.put((t[0]+bc, t[1]+1))
print(-1)
