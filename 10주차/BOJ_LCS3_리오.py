import sys

first = sys.stdin.readline().rstrip()
second = sys.stdin.readline().rstrip()

dp = [[[0] * (len(third)+1) for _ in range(len(second)+1)] for _ in range(len(first)+1)]

for i in range(1, len(first)+1):
    for j in range(1, len(second)+1):

            if (first[i-1] == second[j-1]):
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1], dp[i][j])

print(dp[len(first)][len(second)])
