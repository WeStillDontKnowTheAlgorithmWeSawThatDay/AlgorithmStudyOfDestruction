# * 
# sys.stdin.readline 안쓰면 시간초과

import sys
input = sys.stdin.readline
n, m = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(n)]
xys = [list(map(int, input().split())) for _ in range(m)]

dp = [[0]* (n+1) for _ in range(n+1)]
for i in range(1, n+1):
    for j in range(1, n+1):
        dp[i][j] = dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1] + arr[i-1][j-1]

for x1, y1, x2, y2 in xys:
    sum = dp[x2][y2] - dp[x1-1][y2] - dp[x2][y1-1] + dp[x1-1][y1-1]
    print(sum)
