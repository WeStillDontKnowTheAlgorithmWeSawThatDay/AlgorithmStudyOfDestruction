from collections import deque

m, n, k = map(int, input().split())
board = [[0]*n for _ in range(m)]
for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(x1, x2):
        for j in range(y1, y2):
            board[j][i] = 1

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
areas = []

def bfs(x, y):
    queue = deque()
    queue.append((i, j))
    board[x][y] = 1
    area = 1
    while queue:
        x, y = queue.popleft()
        for l in range(4):
            px, py = x + dx[l], y + dy[l]
            if 0 <= px < m and 0 <= py < n and board[px][py] == 0:
                board[px][py] = 1
                queue.append((px, py))
                area += 1
    areas.append(area)

for i in range(0, m):
    for j in range(0, n):
        if board[i][j] == 0:
            bfs(i, j)
areas.sort()
print(len(areas))
print(*areas)
