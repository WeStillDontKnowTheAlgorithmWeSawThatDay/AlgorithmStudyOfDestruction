import sys

first = sys.stdin.readline().rstrip()
second = sys.stdin.readline().rstrip()
answer = 0
dp = [[0] * (len(second)+1) for _ in range(len(first)+1)]

for i in range(1, len(first)+1):
    for j in range(1, len(second)+1):

        if (first[i-1] == second[j-1]):
            dp[i][j] = dp[i-1][j-1] + 1
            answer = max(answer, dp[i][j])
print(answer)
