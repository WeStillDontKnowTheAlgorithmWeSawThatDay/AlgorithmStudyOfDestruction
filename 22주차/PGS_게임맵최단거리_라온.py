from collections import deque

def solution(maps):
    answer = 0
    
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    
    n, m = len(maps), len(maps[0])
    route = [[0] * m for _ in range(n)]
    
    queue = deque()
    queue.append((0, 0))
    route[0][0] = 1
    
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            px, py = x + dx[i], y + dy[i]
            if (0 <= px < n and 0 <= py < m) and route[px][py] == 0 and maps[px][py] == 1:
                queue.append((px, py))
                if px == n-1 and py == m-1 and route[px][py] != 0:
                    route[px][py] = min(route[px][py], route[x][y] + 1)
                else:
                    route[px][py] = route[x][y] + 1
    if route[n-1][m-1] == 0:
        return -1
    else:
        return route[n-1][m-1]
