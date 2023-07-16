n, k = map(int, input().split())

coins = []
for _ in range(n):
    coins.append(int(input()))
coins.sort()

dp = [0 for _ in range(k + 1)]
dp[0] = 1

for c in coins:
    for i in range(c, k+1):
        if i - c >= 0:
            dp[i] += dp[i-c]

print(dp[k])
