import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
mat = [list(map(int, input().split())) for _ in range(n)]
iceberg = set()

def bfs(x, y):
    visited[x][y] = True
    queue = deque([(x, y)])

    while queue:
        x, y = queue.popleft()

        for cx, cy in (0, 1), (1, 0), (0, -1), (-1, 0):
            nx = x + cx
            ny = y + cy
            if not visited[nx][ny]:
                if mat[nx][ny] == 0 and mat[x][y] != 0:
                    mat[x][y] -= 1

                if mat[nx][ny] != 0:
                    visited[nx][ny] = True
                    queue.append((nx, ny))

        if mat[x][y] == 0:
            iceberg.remove((x, y))
    return

for i in range(n):
    for j in range(m):
        if mat[i][j] != 0:
            iceberg.add((i, j))

year = 0
while True:
    count = 0
    visited = [[False] * m for _ in range(n)]
    for i, j in list(iceberg):  # Convert set to list before iterating to avoid runtime error
        if mat[i][j] != 0 and not visited[i][j]:
            bfs(i, j)
            count += 1
    
    if count >= 2:
        print(year)
        break
        
    if count == 0:
        print(0)
        break
        
    year += 1
