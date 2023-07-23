dx = (0, 1, 0, -1)
dy = (1, 0, -1, 0)


def is_possible(x, y, N):
    return 0 <= x < N and 0 <= y < N


d = 0

N = int(input())
arr = [[0] * N for _ in range(N)]

K = int(input())
for _ in range(K):
    x, y = map(int, input().split())
    arr[x - 1][y - 1] = 1

# for i in range(N):
#     print(*arr[i])

turnList = []

L = int(input())
for _ in range(L):
    turnList.append(list(map(str, input().split())))

print(turnList)

x, y = 0, 0
cnt = 0

arr[x][y] = 2

while True:
    limit, dir = turnList.pop()
    for _ in range(int(limit)):
        x, y = x + dx[d], y + dy[d]
        if is_possible(x, y) or arr[x][y] == 2:
            break
        if is_possible(x, y) and arr[x][y] == 0:

