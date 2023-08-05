from collections import deque

n = int(input())
a, b = map(int, input().split())
m = int(input())
graph = [list(map(int, input().split())) for _ in range(m)]

# print(graph)

queue = deque([[a, 0]])

chk = [0 for _ in range(n + 1)]
chk[a] == 1

while queue:
    now, cnt = queue.popleft()
    if now == b:
        print(cnt)
        exit(0)

    for g in graph:
        if now in g:
            if g[0] == now and chk[g[1]] == 0:
                chk[g[1]] = 1
                queue.append([g[1], cnt + 1])
            if g[1] == now and chk[g[0]] == 0:
                chk[g[0]] = 1
                queue.append([g[0], cnt + 1])

print(-1)
