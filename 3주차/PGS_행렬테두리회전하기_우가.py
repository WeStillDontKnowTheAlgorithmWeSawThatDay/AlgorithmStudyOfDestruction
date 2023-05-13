def solution(rows, columns, queries):
    answer = []
    
    liss = [[0 for i in range(columns)] for j in range(rows)]
    count = 1
    for i in range(0, columns):
        for j in range(0, rows):
            liss[i][j] = count
            count += 1
            
    print(liss)
            
    return 0
