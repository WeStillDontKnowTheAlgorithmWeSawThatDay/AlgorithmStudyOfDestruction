import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(i, j):
    q = deque()
    q.append((i, j))
    visited[i][j] = True
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < n and 0 <= ny < n:
                if not visited[nx][ny] and a[nx][ny] > h:
                    q.append((nx, ny))
                    visited[nx][ny] = True


ans = 0

# 2차원 배열 a의 요소 중 가장 큰 값(최고 높이)까지 반복문
for h in range(max(map(max, a))):
    visited = [[False] * n for _ in range(n)]
    safe = 0
    for i in range(n):
        for j in range(n):
            if not visited[i][j] and a[i][j] > h:
                bfs(i, j)
                safe += 1
    ans = max(ans, safe)

print(ans)
