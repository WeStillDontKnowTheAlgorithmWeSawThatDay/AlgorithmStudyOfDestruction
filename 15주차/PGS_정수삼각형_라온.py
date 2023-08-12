def solution(triangle):
    triangle = triangle[::-1]
    for i, line in enumerate(triangle):
        for j, square in enumerate(line[:len(line)-1]):
            triangle[i+1][j] = triangle[i+1][j] + max(line[j], line[j+1])    
    return triangle[len(triangle)-1][0]

### 이전 풀이
def solution(triangle):
    
    for tri in reversed(triangle[:len(triangle)-1]):
        temp = []
        pop = triangle.pop() # 삼각형 맨 아랫줄 
        for j in range(len(pop)-1):
            temp.append( tri[j] + max(pop[j], pop[j+1]) ) # 왼쪽 오른쪽 중에 큰 거를 더함
        triangle.pop()
        triangle.append(temp)
        
    return triangle[0][0]