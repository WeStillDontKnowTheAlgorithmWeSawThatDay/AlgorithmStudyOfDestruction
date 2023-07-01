# **
# python3는 시간초과, pypy는 ㄱㅊ

first = input()
second = input()

lcs = 0
dp = [[0 for _ in range(len(second) + 1)] for _ in range(len(first) + 1)]

for i in range(1, len(first)+1):
    for j in range(1, len(second)+1):
        if first[i-1] == second[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
            lcs = max(lcs, dp[i][j]) # 시간초과 .. 
print(lcs)
