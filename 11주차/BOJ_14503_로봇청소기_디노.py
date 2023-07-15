dx = (-1, 0, 1, 0)
dy = (0, 1, 0, -1)

N, M = map(int, input().split())
r, c, d = map(int, input().split())

arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))

chk = [[0] * M for _ in range(N)]

for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            chk[i][j] = 1
# for c in chk:
#     print(*c)


# print(r, c)

cnt = 0

while True:
    if arr[r][c] == 0 and chk[r][c] == 0:
        cnt += 1
        chk[r][c] = 1
    if chk[r + dx[0]][c + dy[0]] == 1 and chk[r + dx[1]][c + dy[1]] == 1 and chk[r + dx[2]][c + dy[2]] == 1 and chk[r + dx[3]][c + dy[3]] == 1:
        if arr[r + dx[(d+2) % 4]][c + dy[(d+2) % 4]] == 1:
            break
        else:
            r, c = r + dx[(d+2) % 4], c + dy[(d+2) % 4]
    else:
        d = (d + 3) % 4
        if arr[r + dx[d]][c + dy[d]] == 0 and chk[r + dx[d]][c + dy[d]] == 0:
            r, c = r + dx[d], c + dy[d]
    # print("r, c = ", r, c)

print(cnt)
