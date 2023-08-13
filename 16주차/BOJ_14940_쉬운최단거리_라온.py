# 레전드레전드레전드, 가로 세로 헷갈리지 않기

from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

queue = deque()
visited = [[0 for _ in range(m)] for _ in range(n)]
dist = [[-1 for _ in range(m)] for _ in range(n)]
for i in range(n):
    for j in range(m):
        # 원래 갈 수 없는 곳 
        if board[i][j] == 0:
            dist[i][j] = 0
        if board[i][j] == 2:
            dist[i][j] = 0
            visited[i][j] = 1
            queue.append((i, j))

px = [0, 0, 1, -1]
py = [1, -1, 0, 0]

while queue:
    x, y = queue.popleft()

    for i in range(4):
        pos_x, pos_y = x + px[i], y + py[i]
        if pos_x < 0 or pos_x >= n or pos_y < 0 or pos_y >= m:
            continue
        if visited[pos_x][pos_y] == 0 and board[pos_x][pos_y] == 1:
            queue.append((pos_x, pos_y))
            visited[pos_x][pos_y] = 1
            dist[pos_x][pos_y] = dist[x][y] + 1

for line in dist:
    print(*line)

