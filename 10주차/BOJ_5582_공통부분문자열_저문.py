first = input()
second = input()

dp = []
for _ in range(len(first)):
    dp.append([0] * len(second))

answer = 0
for i in range(len(first)):
    for j in range(len(second)):
        if first[i] == second[j]:
            if i == 0 or j == 0:
                dp[i][j] = 1
            else:
                dp[i][j] = dp[i-1][j-1] + 1
            answer = max(answer, dp[i][j])

print(answer)
