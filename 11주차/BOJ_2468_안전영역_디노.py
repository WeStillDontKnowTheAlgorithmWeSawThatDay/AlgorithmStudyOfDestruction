dx = (0, 1, 0, -1)
dy = (1, 0, -1, 0)


def is_possible(x, y, n):
    return 0 <= x < n and 0 <= y < n


N = int(input())

arr = []
minFlood, maxFlood = 10000000, 0
for _ in range(N):
    tmp = list(map(int, input().split()))
    minFlood = min(minFlood, min(tmp))
    maxFlood = max(maxFlood, max(tmp))
    arr.append(tmp)

# print(maxFlood, minFlood)

ans = 1

for f in range(minFlood, maxFlood):
    chk = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if arr[i][j] <= f:
                chk[i][j] = 1

    cnt = 0

    for i in range(N):
        for j in range(N):
            if chk[i][j] == 0:
                cnt += 1
                stk = [[i, j]]
                while stk:
                    x, y = stk.pop()
                    for k in range(4):
                        nx, ny = x + dx[k], y + dy[k]
                        if is_possible(nx, ny, N) and chk[nx][ny] == 0:
                            chk[nx][ny] = 1
                            stk.append([nx, ny])
    ans = max(ans, cnt)


print(ans)
