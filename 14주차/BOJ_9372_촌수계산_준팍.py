import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
A, B = map(int, input().split())

M = int(input())
graph = [[] for _ in range(N+1)]

for _ in range(M):
  x, y = map(int, input().split())  
  graph[x].append(y)
  graph[y].append(x)

def find_chonsu(n, target1, target2, graph):
    queue = deque([(target1, 0)])
    visited = [False] * (n+1)
    visited[target1] = True

    while queue:
        current, chonsu = queue.popleft()
        if current == target2:
            return chonsu

        for next_node in graph[current]:
            if not visited[next_node]:
                queue.append((next_node, chonsu+1))
                visited[next_node] = True

    return -1

print(find_chonsu(N, A, B, graph))
