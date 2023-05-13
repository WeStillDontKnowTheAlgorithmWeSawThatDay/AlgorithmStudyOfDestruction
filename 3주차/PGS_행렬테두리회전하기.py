from collections import deque

def solution(rows, columns, queries):
    answer = []
    matrix = [[columns*(row) + column+1 for column in range(columns)] for row in range(rows)]
    
    for x1,y1,x2,y2 in queries:
        target, num = [], []
        
        for y in range(y1, y2+1, 1):
            # print("가로1:", x1, y)
            target.append((x1, y))
            num.append(matrix[x1-1][y-1])
        
        for x in range(x1+1, x2, 1):
            # print("세로1:", x, y2)
            target.append((x, y2))
            num.append(matrix[x-1][y2-1])
        
        for y in range(y2, y1, -1):
            # print("가로2:", x2, y)
            target.append((x2, y)) 
            num.append(matrix[x2-1][y-1])
        
        for x in range(x2, x1, -1):
            # print("세로2:", x, y1)
            target.append((x, y1))
            num.append(matrix[x-1][y1-1])
        
        target = deque(target)
        target.append(target.popleft())
        answer.append(min(num))
    
        for i,(n,m) in enumerate(target):
            matrix[n-1][m-1] = num[i]
    return answer

# (x1, y1), (x2, y2)
# (2, 2), (5, 4)
# (2, 2) ~ (2, 4) 가로1 y+=1, 4를 넘어가는 경우 x+=1
# (2, 4) ~ (5, 4) 세로1 x+=1, 5를 넘어가는 경우 y-=1
# (5, 4) ~ (5, 2) 가로2 x-=1, 2보다 작아지는 경우 y+=1
# (5, 2) ~ (2, 2) 세로2 y-=1, 2보다 작아지는 경우 x-=1
