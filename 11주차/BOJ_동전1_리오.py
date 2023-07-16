n,k = map(int, input().split())

c = [int(input()) for i in range(n)]

dp = [0 for i in range(k+1)]
dp[0] = 1

for i in c :
    for j in range(i, k+1) :
        if j-i >= 0 :
            dp[j] += dp[j-i]
print(dp[k])
1
