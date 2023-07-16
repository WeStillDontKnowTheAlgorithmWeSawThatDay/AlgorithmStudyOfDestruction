# pypy로 돌려야 통과함므
import copy

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

dx = (0, 1, 0, -1)
dy = (1, 0, -1, 0)


def is_possible(x, y):
    return 0 <= x < N and 0 <= y < M


def cnt_bingsan(arr, n, m):
    cnt = 0
    chk = [[0] * M for _ in range(N)]
    for i in range(n):
        for j in range(m):
            stack = []
            if arr[i][j] > 0 and chk[i][j] == 0:
                cnt += 1
                chk[i][j] = 1
                stack.append([i, j])
            while stack:
                x, y = stack.pop()
                for k in range(4):
                    nx, ny = x + dx[k], y + dy[k]
                    if is_possible(nx, ny) and chk[nx][ny] == 0 and arr[nx][ny] > 0:
                        chk[nx][ny] = 1
                        stack.append([nx, ny])
    # print("cnt = ", cnt)
    return cnt


ans = 0
while True:
    ans += 1
    tmp = [[0] * M for _ in range(N)]

    for i in range(N):
        for j in range(M):
            dct = 0
            for k in range(4):
                nx, ny = i + dx[k], j + dy[k]
                if is_possible(nx, ny) and arr[nx][ny] == 0:
                    dct += 1

            # print("arr[i][j]", arr[i][j])
            ah = arr[i][j] - dct
            # print(ah)
            if ah < 0:
                ah = 0
            tmp[i][j] = ah

    # print(tmp)
    arr = copy.deepcopy(tmp)

    # print("cnt_bingsan", cnt_bingsan(arr, N, M))
    # for ii in range(N):
    #     print(*arr[ii])
    # print(ans)

    if cnt_bingsan(arr, N, M) >= 2:
        print(ans)
        break

    tri = 0
    for i in range(N):
        if sum(arr[i]) > 0:
            tri += 1
    if tri > 0:
        continue
    print(0)
    break
