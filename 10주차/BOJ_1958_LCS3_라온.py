# *** too hard
# 못품 
first, second, third = input(), input(), input()
strings = [first, second, third]
strings.sort(key=lambda x : len(x))

str1, str2, str3 = strings[0], strings[1], strings[2]
dp = [[0 for _ in range(len(str2) + 1)] for _ in range(len(str1) + 1)]

lcs = 0
for i in range(1, len(str1) + 1):
    for j in range(1, len(str2) + 1):
        if str1[i-1] == str2[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

def func(dp):
    for i in range(len(str1), 0, -1):
        for j in range(len(str2), 0, -1):
            # print(dp[i][j])
            temp = max(dp[i-1][j], dp[i][j-1])
            # if temp == dp[i][j]:
                

strs = []
func(dp)

# dp = [[0 for _ in range(len(str2) + 1)] for _ in range(len(str3) + 1)]
