def check_bingo(board):
    num = 0
    left, right = 0, 0
    for i in range(5):
        row, column = 0, 0
        for j in range(5):
            if board[i][j] == 1:    row += 1
            if board[j][i] == 1:    column += 1

        if board[i][i] == 1:    left += 1
        if board[i][4-i] == 1:    right += 1

        if row == 5:    num += 1
        if column == 5: num += 1

    if left == 5: num += 1
    if right == 5: num += 1
    return num

hash = {}
for i in range(5):
    line = list(map(int, input().split()))
    for j in range(len(line)):
        hash[line[j]] = 5*i + j
number = [list(map(int, input().split())) for _ in range(5)]

board = [[0]*5 for _ in range(5)]
answer = 0
for i in range(5):
    for j in range(5):
        pos = hash[number[i][j]]
        x = pos//5
        y = pos - x*5
        board[x][y] = 1
        if check_bingo(board) >= 3:
            answer = (5*i)+j+1
            break
    if answer >= 3: break
print(answer)
