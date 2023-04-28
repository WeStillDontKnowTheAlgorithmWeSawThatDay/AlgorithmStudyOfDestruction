def solution(line):
    answer = []

    points = []
    for i in range(len(line)):
        for j in range(len(line)):
            a, b, e = line[i]
            c, d, f = line[j]
            if i == j:
                continue
            if (a * d - b * c) == 0:
                continue

            x = (b * f - e * d) / (a * d - b * c)
            y = (e * c - a * f) / (a * d - b * c)

            if x % 1 != 0 or y % 1 != 0:
                continue

            points.append((int(x), int(y)))

    points = list(set(points))

    new_points = []
    for point in points:
        x, y = point
        new_points.append([x, y])

    x_list = []
    y_list = []
    for point in points:
        x_list.append(point[0])
        y_list.append(point[1])

    x_length = max(x_list) - min(x_list) + 1
    y_length = max(y_list) - min(y_list) + 1

    for i in range(y_length):
        level = ""
        for j in range(x_length):
            level += "."
        answer.append(level)

    for point in new_points:
        point[0] = abs(point[0] + -min(x_list))
        point[1] = abs(point[1] + -max(y_list))
        answer[point[1]] = list(answer[point[1]])
        answer[point[1]][point[0]] = "*"
        answer[point[1]] = ''.join(answer[point[1]])

    return answer