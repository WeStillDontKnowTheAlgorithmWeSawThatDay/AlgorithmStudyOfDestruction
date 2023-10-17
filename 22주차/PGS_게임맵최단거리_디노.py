from collections import deque

dx = (0, 1, 0, -1)
dy = (1, 0, -1, 0)


def is_possible(x, y, n, m):
    return 0 <= x < n and 0 <= y < m


def solution(maps):
    answer = 0
    dq = deque([[0, 0]])

    while dq:
        x, y = dq.popleft()

        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            if is_possible(nx, ny, len(maps), len(maps[0])) and maps[nx][ny] == 1:
                if nx == len(maps) - 1 and ny == len(maps[0]) - 1:
                    return maps[x][y] + 1
                maps[nx][ny] = maps[x][y] + 1
                dq.append([nx, ny])
    return -1
