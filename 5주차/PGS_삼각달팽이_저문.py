def solution(n):
    answer = []

    snail = []
    for i in range(n):
        temp = []
        for j in range(n):
            temp.append(0)
        snail.append(temp)

    row, col, count = -1, 0, 1

    for i in range(n):
        for _ in range(n-i):
            if i % 3 == 0:
                row += 1
            elif i % 3 == 1:
                col += 1
            else:
                row -= 1
                col -= 1

            snail[row][col] = count
            count += 1

    for i in range(n):
        for j in range(i + 1):
            answer.append(snail[i][j])

    return answer