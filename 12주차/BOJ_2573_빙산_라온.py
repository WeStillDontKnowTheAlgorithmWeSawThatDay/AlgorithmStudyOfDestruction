# python3 로는 시간초과, pypy3로는 통과

import copy
from collections import deque

n, m = map(int, input().split())
north = [list(map(int, input().split()))for _ in range(n)]
dir = [[1, 0], [-1, 0], [0, 1], [0, -1]]

def bfs(north):
    queue = deque()
    visited = [[0]*m for _ in range(n)]

    for x in range(1, n):
        for y in range(1, m):
            if north[x][y] > 0:
                visited[x][y] = 1
                queue.append([x, y])
                break
        if queue:   break

    num = 1
    while queue:
        i, j = queue.popleft()        
        for x, y in dir:
            if north[i+x][j+y] > 0 and visited[i+x][j+y] == 0:
                queue.append([i+x, j+y])
                visited[i+x][j+y] = 1

        if len(queue) == 0:
            for x in range(1, n):
                for y in range(1, m):
                    if north[x][y] > 0 and visited[x][y] == 0:
                        queue.append([x, y])
                        visited[x][y] = 1
                        num += 1
                        return num
    return num

def check_empty(north):
    for i in range(1, n):
        for j in range(1, m):
            if north[i][j] > 0:
                return False
    return True

num = 0
while(True):
    temp = copy.deepcopy(north)

    for i in range(1, n):
        for j in range(1, m):
            if temp[i][j] == 0:    
                continue
            for x, y in dir:
                if north[i][j] <= 0:    break
                if temp[i+x][j+y] == 0 and temp[i][j] > 0:
                    north[i][j] -= 1
    num += 1
    if bfs(north) >= 2: break
    if check_empty(north):
        num = 0
        break
print(num)