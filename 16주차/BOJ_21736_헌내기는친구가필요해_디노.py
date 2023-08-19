from collections import deque

dx = (0, 1, 0, -1)
dy = (1, 0, -1, 0)


def is_possible(x, y, n, m):
    return 0 <= x < n and 0 <= y < m


N, M = map(int, input().split())
arr = [[*input()] for _ in range(N)]

cnt = 0

for i in range(N):
    for j in range(M):
        if arr[i][j] == "I":
            dq = deque([[i, j]])
            chk = [[0] * M for _ in range(N)]
            chk[i][j] = 1
            while dq:
                x, y = dq.popleft()
                for d in range(4):
                    nx, ny = x + dx[d], y + dy[d]
                    if is_possible(nx, ny, N, M) and chk[nx][ny] == 0 and arr[nx][ny] != 'X':
                        if arr[nx][ny] == "P":
                            cnt += 1
                        chk[nx][ny] = 1
                        dq.append([nx, ny])

if cnt == 0:
    print("TT")
else:
    print(cnt)
