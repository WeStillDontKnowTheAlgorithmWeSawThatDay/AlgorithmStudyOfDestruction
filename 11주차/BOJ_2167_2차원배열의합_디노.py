N, M = map(int, input().split())
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))

dp = [[0] * (M + 1) for _ in range(N + 1)]

# 누적합은 이거면 끝
for i in range(N + 1):
    for j in range(M + 1):
        dp[i][j] = arr[i - 1][j - 1] + dp[i - 1][j] + dp[i][j - 1] - dp[i - 1][j - 1]

K = int(input())
for _ in range(K):
    i, j, x, y = map(int, input().split())
    print(dp[x][y] - dp[i - 1][y] - dp[x][j - 1] + dp[i - 1][j - 1])
