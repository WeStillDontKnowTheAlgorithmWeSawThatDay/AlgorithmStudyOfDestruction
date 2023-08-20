def dfs(n, computers, visited):
    for i, com in enumerate(computers[n]):
        if com == 1 and i != n and not visited[i]:
            visited[i] = 1
            visited = dfs(i, computers, visited)
    return visited
    
def solution(n, computers):
    answer = 0
    visited = [0] * n
    visited[0] = 1
    next = 0
    while next != -1:
        visited = dfs(next, computers, visited)
        answer += 1
        next = -1
        for i, visit in enumerate(visited):
            if visit == 0:
                next = i
                visited[i] = 1
                break  
    return answer

''' 
# 이전풀이
def dfs(computers, node, visited):

    visited[node] = 1
    computer = computers[node]
    for i in range(len(computer)):
        if computer[i] == 1 and i != node and visited[i] == 0:
            visited[i] = 1
            dfs(computers, i, visited)

def solution(n, computers):

    visited = [0]*n
    answer = 0
    for node in range(n):
        if visited[node] == 0: 
            dfs(computers, node, visited)
            answer += 1
    return answer
'''