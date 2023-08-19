from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
board = [list(input()) for _ in range(n)]
visited = [[0] * m for _ in range(n)]

queue = deque()
for i in range(n):
    for j in range(m):
        if board[i][j] == 'I':
            queue.append((i, j))
            visited[i][j] = 1

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

answer = 0
while queue:
    x, y = queue.popleft()
    for i in range(4):
        px, py = x + dx[i], y + dy[i]
        if 0 <= px < n and 0 <= py < m and visited[px][py] == 0 and (board[px][py] == 'O' or board[px][py] == 'P'):
            if board[px][py] == 'P':
                answer += 1
            queue.append((px, py))
            visited[px][py] = 1

if answer == 0:
    print('TT')
else:
    print(answer)