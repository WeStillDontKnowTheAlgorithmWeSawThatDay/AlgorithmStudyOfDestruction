from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
array = [list(map(int, input().split())) for _ in range(n)]

maximum = 1
for arr in array:
    maximum = max(maximum, max(arr))

height = 1
max_num = 1
queue = deque()
while height <= maximum:
    num = 0
    visited = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
                if array[i][j] <= height or visited[i][j] != 0:
                    continue
                queue.append((i, j))
                while queue:
                    x, y = queue.popleft()
                    visited[x][y] = 1
                    if x > 0 and visited[x-1][y] == 0 and array[x-1][y] > height:
                        queue.append((x-1, y))
                        visited[x-1][y] = 1
                    if y > 0 and visited[x][y-1] == 0 and array[x][y-1] > height:
                        queue.append((x, y-1))
                        visited[x][y-1] = 1
                    if x+1 < n and visited[x+1][y] == 0 and array[x+1][y] > height:
                        queue.append((x+1, y))
                        visited[x+1][y] = 1
                    if y+1 < n and visited[x][y+1] == 0 and array[x][y+1] > height:
                        queue.append((x, y+1))
                        visited[x][y+1] = 1
                num += 1
    height += 1
    max_num = max(max_num, num)
print(max_num)