def solution(n):
    answer = []
    list = [[0] * n for _ in range(n)]
    x, y = -1, 0
    num = 1
    
    for i in range(n):
        for _ in range(i, n):
            if i % 3 == 0:
                x += 1
            elif i % 3 == 1: 
                y += 1
            elif i % 3 == 2:
                x -= 1
                y -= 1
            list[x][y] = num
            num += 1
    for i in list:
        for j in i:
            if j:
                answer.append(j)
    return answer
