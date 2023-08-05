from collections import deque
import copy

n, m = map(int, input().split())
grid = [list(input()) for _ in range(n)]


# print(grid)

def is_possible(x, y):
    return 0 <= x < n and 0 <= y < m


def move(ar, d):
    arr = copy.deepcopy(ar)
    tri = 0
    if d == 0:  # 동
        for i in range(n):
            for j in range(m - 1, -1, -1):
                if arr[i][j] == 'R' or arr[i][j] == 'B':
                    k = 1
                    while is_possible(i, j + k) and arr[i][j + k] == '.':
                        k += 1

                    if arr[i][j + k] == 'O':
                        if arr[i][j] == 'R':
                            arr[i][j] = '.'
                            tri = 1
                        elif arr[i][j] == 'B':
                            arr[i][j] = '.'
                            tri = -1
                    else:
                        if k == 1:
                            continue
                        arr[i][j + k - 1] = arr[i][j]
                        arr[i][j] = '.'

    elif d == 1:  # 서
        for i in range(n):
            for j in range(m):
                if arr[i][j] == 'R' or arr[i][j] == 'B':
                    k = 1
                    while is_possible(i, j - k) and arr[i][j - k] == '.':
                        k += 1

                    if arr[i][j - k] == 'O':
                        if arr[i][j] == 'R':
                            arr[i][j] = '.'
                            tri = 1
                        elif arr[i][j] == 'B':
                            arr[i][j] = '.'
                            tri = -1
                    else:
                        if k == 1:
                            continue
                        arr[i][j - k + 1] = arr[i][j]
                        arr[i][j] = '.'
    elif d == 2:  # 남
        for i in range(n - 1, -1, -1):
            for j in range(m):
                if arr[i][j] == 'R' or arr[i][j] == 'B':
                    k = 1
                    while is_possible(i + k, j) and arr[i + k][j] == '.':
                        k += 1

                    if arr[i + k][j] == 'O':
                        if arr[i][j] == 'R':
                            arr[i][j] = '.'
                            tri = 1
                        elif arr[i][j] == 'B':
                            arr[i][j] = '.'
                            tri = -1
                    else:
                        if k == 1:
                            continue
                        arr[i + k - 1][j] = arr[i][j]
                        arr[i][j] = '.'
    elif d == 3:  # 북
        for i in range(n):
            for j in range(m):
                if arr[i][j] == 'R' or arr[i][j] == 'B':
                    k = 1
                    while is_possible(i - k, j) and arr[i - k][j] == '.':
                        k += 1
                    if arr[i - k][j] == 'O':
                        if arr[i][j] == 'R':
                            arr[i][j] = '.'
                            tri = 1
                        elif arr[i][j] == 'B':
                            arr[i][j] = '.'
                            tri = -1
                    else:
                        if k == 1:
                            continue
                        arr[i - k + 1][j] = arr[i][j]
                        arr[i][j] = '.'
    return (tri, arr)


# for i in range(4):
#     tmp = move(grid,i)
#     print(tmp[0])
#     for j in range(n):
#         print(*tmp[1][j])
#     print()


dq = deque()
dq.append([0, grid, 5])

while dq:
    cnt, now_grid, back = dq.popleft()
    if cnt > 10:
        continue
    for i in range(4):
        if back == i:
            continue
        n_grid = copy.deepcopy(now_grid)
        n_tri, nx_grid = move(n_grid, i)
        if n_tri == 1:
            print(cnt + 1)
            exit(0)
        elif n_tri == 0:
            dq.append([cnt + 1, nx_grid, i])
    # for j in range(n):
    #     print(*now_grid[j])
    # print()

print(-1)
