## **

from collections import deque
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

m, n = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(m)]

def dfs(stack):
    if not stack:
        return 0
    i, j = stack.pop()
    if (i, j) == (m-1, n-1):
        return 1
    answer = 0
    for dir in dirs:
        x, y = i + dir[0], j + dir[1]
        if 0 <= x < m and 0 <= y < n and maps[x][y] < maps[i][j]:
            if dp[x][y] >= 0:
                answer += dp[x][y]
            else:
                stack.append((x, y))
                answer += dfs(stack)
    dp[i][j] = answer
    return answer
    

stack = [(0, 0)]
dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
dp = [[-1]* n for _ in range(m)]
dp[0][0] = 0
print(dfs(stack))
