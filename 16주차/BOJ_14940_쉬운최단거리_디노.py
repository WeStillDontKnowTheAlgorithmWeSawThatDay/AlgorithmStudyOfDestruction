import sys
from collections import deque

input = sys.stdin.readline

dx = (0, 1, 0, -1)
dy = (1, 0, -1, 0)


def is_possible(x, y, n, m):
    return 0 <= x < n and 0 <= y < m


n, m = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(n)]
ans = [[-1] * m for _ in range(n)]


for i in range(n):
    for j in range(m):
        if arr[i][j] == 0:
            ans[i][j] = 0

for i in range(n):
    for j in range(m):
        if arr[i][j] == 2:
            ans[i][j] = 0
            dq = deque([[i, j, 0]])
            chk = [[0] * m for _ in range(n)]
            chk[i][j] = 1
            while dq:
                x, y, cnt = dq.popleft()
                for d in range(4):
                    nx, ny = x + dx[d], y + dy[d]
                    if is_possible(nx, ny, n, m) and arr[nx][ny] == 1 and chk[nx][ny] == 0:
                        chk[nx][ny] = 1
                        ans[nx][ny] = cnt + 1
                        dq.append([nx, ny, cnt + 1])


for a in ans:
    print(*a)