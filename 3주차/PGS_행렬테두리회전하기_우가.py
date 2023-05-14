def solution(rows, columns, queries):
    answer = []
    
    liss =  [[0] * columns for _ in range(rows)]
    count = 1

    for i in range(0, rows):
        for j in range(0, columns):
            liss[i][j] = count
            count += 1

    for x1, y1, x2, y2 in queries:
        x1 = x1 - 1
        x2 = x2 - 1
        y1 = y1 - 1
        y2 = y2 - 1

        temp = liss[x1][y1]
        tempte = temp

        for i in range(x1, x2):
            tempp = liss[i + 1][y1]
            liss[i][y1] = tempp
            tempte = min(tempte, tempp)
            
        for i in range(y1, y2):
            tempp = liss[x2][i + 1]
            liss[x2][i] = tempp
            tempte = min(tempte, tempp)
            
        for i in range(x2, x1, -1):
            tempp = liss[i - 1][y2]
            liss[i][y2] = tempp
            tempte = min(tempte, tempp)

        for i in range(y2, y1, -1):
            tempp = liss[x1][i - 1]
            liss[x1][i] = tempp
            tempte = min(tempte, tempp)


        liss[x1][y1 + 1] = temp
        answer.append(tempte)

            
    return answer
