from collections import deque
import sys
input = sys.stdin.readline

# 입력
N = int(input())
board = []
for _ in range(N):
    board.append(list(map(int, input().split())))

# 높이 1 ~ 100까지 BFS 탐색
direction = [(1,0), (-1,0), (0,1), (0,-1)]
res = 0  # 안전 구역
for high in range(0, 101):
    visited = [[False]*N for _ in range(N)]
    queue = deque([])
    cnt = 0  # 안전구역

    for i in range(N):
        for j in range(N):
            if not visited[i][j] and board[i][j] > high:
                cnt += 1
                queue.append((i, j))
                while queue:
                    x, y = queue.popleft()
                    for dx, dy in direction:
                        nx, ny = x+dx, y+dy
                        if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and board[nx][ny] > high:
                            visited[nx][ny] = True
                            queue.append((nx, ny))
    # print(high, cnt)
    res = max(res, cnt)
print(res)
