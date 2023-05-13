def spin(x1, y1, x2, y2, matrix):
    all = []
    temp = matrix[x1][y1]
    all.append(temp)

    for i in range(x1, x2):
        matrix[i][y1] = matrix[i + 1][y1]
        all.append(matrix[i + 1][y1])

    for i in range(y1, y2):
        matrix[x2][i] = matrix[x2][i + 1]
        all.append(matrix[x2][i + 1])

    for i in range(x2, x1, -1):
        matrix[i][y2] = matrix[i - 1][y2]
        all.append(matrix[i - 1][y2])

    for i in range(y2, y1 + 1, -1):
        matrix[x1][i] = matrix[x1][i - 1]
        all.append(matrix[x1][i - 1])

    matrix[x1][y1 + 1] = temp
    return min(all)


def solution(rows, columns, queries):
    answer = []

    matrix = []
    for i in range(rows):
        row = []
        for j in range(columns):
            row.append(columns * i + (j + 1))
        matrix.append(row)

    for query in queries:
        answer.append(spin(query[0] - 1, query[1] - 1, query[2] - 1, query[3] - 1, matrix))

    return answer
