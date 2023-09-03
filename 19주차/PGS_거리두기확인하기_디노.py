# 너무 못생겼다 .. 개선 필요

dx = (0, 1, 0, -1)
dy = (1, 0, -1, 0)


def is_possible(x, y):
    return 0 <= x < 5 and 0 <= y < 5


def solution(places):
    answer = []

    for place in places:
        isSafe = 1
        for i in range(5):
            tmp = 0
            for j in range(5):
                if place[i][j] == 'P':
                    tri = 1
                    chk = [[0] * 5 for _ in range(5)]
                    chk[i][j] = 1
                    stack = [[i, j, 0]]

                    end = 0
                    while stack:
                        x, y, cnt = stack.pop()
                        # print(x, y, cnt)
                        for d in range(4):
                            nx, ny = x + dx[d], y + dy[d]
                            if is_possible(nx, ny) and chk[nx][ny] == 0 and place[nx][ny] != 'X':
                                if place[nx][ny] == 'P':
                                    end = 1
                                    break
                                chk[nx][ny] = 1
                                if cnt < 1:
                                    stack.append([nx, ny, cnt + 1])
                        if end == 1:
                            tri = 0
                            break

                    if tri == 0:
                        tmp = 1
                        isSafe = 0
                        break
                if tmp == 1:
                    break
        if isSafe == 1:
            answer.append(1)
        else:
            answer.append(0)
    return answer
