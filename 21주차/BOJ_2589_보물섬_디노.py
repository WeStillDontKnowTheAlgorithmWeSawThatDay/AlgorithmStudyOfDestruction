from collections import deque

dx = (0, 1, 0, -1)
dy = (1, 0, -1, 0)


def is_possible(x, y, n, m):
    return 0 <= x < n and 0 <= y < m


n, m = map(int, input().split())

arr = []
for _ in range(n):
    arr.append(input())

ans = 0

for i in range(n):
    for j in range(m):
        # print(i, j)
        if arr[i][j] == "L":
            if is_possible(i-1, j, n, m) and arr[i-1][j] == "L" and is_possible(i+1, j, n, m) and arr[i+1][j] == "L":
                ans = max(ans, 2)
                continue
            if is_possible(i, j-1, n, m) and arr[i][j-1] == "L" and is_possible(i, j+1, n, m) and arr[i][j+1] == "L":
                ans = max(ans, 2)
                continue
            dq = deque([[i, j, 0]])
            chk = [[0] * m for _ in range(n)]
            chk[i][j] = 1
            tri = 0
            while dq:
                x, y, cnt = dq.popleft()
                for d in range(4):
                    nx, ny = x + dx[d], y + dy[d]
                    if is_possible(nx, ny, n, m) and arr[nx][ny] == "L" and chk[nx][ny] == 0:
                        chk[nx][ny] = 1
                        dq.append([nx, ny, cnt + 1])
                        ans = max(ans, cnt + 1)

print(ans)
