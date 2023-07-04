import sys

input = sys.stdin.readline

str1, str2 = input().strip(), input().strip()
len1, len2 = len(str1), len(str2)

answer = 0

dp = [[0] * (len2 + 1 ) for __ in range(len1+1)]

for i in range(1, len1+1):
    for j in range(1, len2+1):
        if str1[i-1] == str2[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
            answer = max(answer, dp[i][j])
                   
print(answer)
