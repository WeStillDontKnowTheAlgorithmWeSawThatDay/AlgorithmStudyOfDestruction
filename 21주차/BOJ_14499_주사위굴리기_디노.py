dx = (0, 0, -1, 1)
dy = (1, -1, 0, 0)


def is_possible(x, y, n, m):
    return 0 <= x < n and 0 <= y < m


N, M, x, y, K = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]

order = list(map(int, input().split()))

# for i in range(N):
#     print(*arr[i])

up, down, e, n, w, s = 0, 0, 0, 0, 0, 0

# up
# w
# e

for o in order:
    nx, ny = x + dx[o - 1], y + dy[o - 1]
    if is_possible(nx, ny, N, M):
        if o == 1:
            up, e, w, n, s, down = s, e, w, up, down, n
        if o == 2:
            up, e, w, n, s, down = n, e, w, down, up, s
        if o == 3:
            up, e, w, n, s, down = w, up, down, n, s, e
        if o == 4:
            up, e, w, n, s, down = e, down, up, n, s, w
        if arr[nx][ny] == 0:
            arr[nx][ny] = down
        else:
            down = arr[nx][ny]
            arr[nx][ny] = 0
        print(up)
        x, y = nx, ny
