n, m = map(int, input().split())
x, y, now = map(int, input().split())

array = [list(map(int, input().split())) for _ in range(n)]
direction = [(-1, 0), (0, 1), (1, 0), (0, -1)]

num = 0

def blank(i, j):
    return array[i-1][j] and array[i+1][j] and array[i][j-1] and array[i][j+1]


while (True):
    if array[x][y] == 0:
        array[x][y] = 8
        num += 1

    # 주변의 4칸 중 청소되지 않은 빈 칸이 없는 경우
    if blank(x,y) != 0:
        temp_x = x-direction[now][0]
        temp_y = y-direction[now][1]
        if array[temp_x][temp_y] == 1:
            break
        else:
            x = temp_x
            y = temp_y

    # 주변의 4칸 중 청소되지 않은 빈 칸이 있는 경우
    elif blank(x,y) == 0:
        if now == 0:
            now = 3
        else:
            now -= 1

        temp_x = x+direction[now][0]
        temp_y = y+direction[now][1]
        if array[temp_x][temp_y] == 0:
            x = temp_x
            y = temp_y

print(num)