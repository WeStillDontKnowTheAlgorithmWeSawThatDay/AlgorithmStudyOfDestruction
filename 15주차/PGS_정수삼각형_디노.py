def solution(triangle):
    dp = [[0] * n for n in range(1, len(triangle) + 1)]
    dp[0][0] = triangle[0][0]

    for i in range(len(triangle) - 1):
        for j in range(i + 1):
            dp[i + 1][j] = max(dp[i][j] + triangle[i + 1][j], dp[i + 1][j])
            dp[i + 1][j + 1] = max(dp[i][j] + triangle[i + 1][j + 1], dp[i + 1][j + 1])
    # print(dp)

    return max(dp[len(triangle) - 1])
