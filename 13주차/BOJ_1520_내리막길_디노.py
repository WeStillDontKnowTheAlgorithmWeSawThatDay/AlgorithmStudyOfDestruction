import heapq

dx = (1, 0, -1, 0)
dy = (0, 1, 0, -1)

M, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(M)]

# for i in range(M):
#     print(*arr[i])

H = 0

dp = [[-1] * N for _ in range(M)]


def is_possible(x, y, M, N):
    return 0 <= x < M and 0 <= y < N


def dfs(x, y):
    if x == M - 1 and y == N - 1:
        return 1

    if dp[x][y] != -1:
        return dp[x][y]

    cnt = 0
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if is_possible(nx, ny, M, N) and arr[x][y] > arr[nx][ny]:
            cnt += dfs(nx, ny)
    dp[x][y] = cnt
    return dp[x][y]


print(dfs(0, 0))




# 시간초과
# import heapq
#
# dx = (1, 0, -1, 0)
# dy = (0, 1, 0, -1)
#
# M, N = map(int, input().split())
# arr = [list(map(int, input().split())) for _ in range(M)]
#
# # for i in range(M):
# #     print(*arr[i])
#
# H = 0
#
# dp = [[-1] * N for _ in range(M)]
#
#
# def is_possible(x, y, M, N):
#     return 0 <= x < M and 0 <= y < N
#
# cnt = 0
# stk = [[0, 0]]
#
# while stk:
#     x, y = heapq.heappop(stk)
#     for i in range(4):
#         nx, ny = x + dx[i], y + dy[i]
#         if is_possible(nx, ny, M, N) and arr[x][y] > arr[nx][ny]:
#             if nx == M - 1 and ny == N - 1:
#                 cnt += 1
#                 continue
#             heapq.heappush(stk, [nx, ny])
#
# print(cnt)
