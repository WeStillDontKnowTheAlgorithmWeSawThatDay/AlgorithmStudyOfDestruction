import sys
import heapq

input = sys.stdin.readline
INF = sys.maxsize


def dijkstra(st, end):
    q = []
    node = [INF] * (N + 1)
    heapq.heappush(q, (0, st))
    node[st] = 0

    while q:
        d, now = heapq.heappop(q)
        # print(d, now)
        if node[now] < d:
            continue

        for i in arr[now]:
            dst = i[0]
            cost = d + i[1]

            if cost < node[dst]:
                # print("sdaf")
                heapq.heappush(q, (cost, dst))
                node[dst] = cost

    return node[end]


N, M, X = map(int, input().split())

arr = [[] for _ in range(N + 1)]

for _ in range(M):
    i, j, w = map(int, input().split())
    arr[i].append([j, w])

t = 0

for i in range(1, N + 1):
    if i == X:
        continue
    t = max(t, dijkstra(i, X) + dijkstra(X, i))

print(t)
