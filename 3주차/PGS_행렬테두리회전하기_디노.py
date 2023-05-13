def solution(rows, columns, queries):
    answer = []
    arr = []
    cnt = 1
    for _ in range(rows):
        arr.append([cnt + x for x in range(columns)])
        cnt += columns

    for q in queries:
        x1, y1, x2, y2 = q
        x_len, y_len = x2 - x1, y2 - y1
        num_list = []
        s_x, s_y = x1 - 1, y1 - 1

        tmp = arr[s_x][s_y]
        for i in range(1, y_len + 1):
            tmp = arr[s_x][s_y + i]
            num_list.append(tmp)
        s_y += y_len

        for i in range(1, x_len + 1):
            tmp = arr[s_x + i][s_y]
            num_list.append(tmp)
        s_x += x_len

        for i in range(1, y_len + 1):
            tmp = arr[s_x][s_y - i]
            num_list.append(tmp)
        s_y -= y_len

        for i in range(1, x_len + 1):
            tmp = arr[s_x - i][s_y]
            num_list.append(tmp)
        s_x -= x_len

        answer.append(min(num_list))

        cnt = -1
        for i in range(1, y_len + 1):
            arr[s_x][s_y + i] = num_list[cnt]
            cnt += 1
        s_y += y_len

        for i in range(1, x_len + 1):
            arr[s_x + i][s_y] = num_list[cnt]
            cnt += 1
        s_x += x_len

        for i in range(1, y_len + 1):
            arr[s_x][s_y - i] = num_list[cnt]
            cnt += 1
        s_y -= y_len

        for i in range(1, x_len + 1):
            arr[s_x - i][s_y] = num_list[cnt]
            cnt += 1
        s_x -= x_len

    return answer
