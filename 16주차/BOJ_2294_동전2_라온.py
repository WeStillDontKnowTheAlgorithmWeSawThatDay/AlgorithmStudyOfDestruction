# ***, 풀이봄 어렵다

n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]
coins.sort()
dp = [10001]*(k+1)
dp[0] = 0

for i in range(1, k+1):
    for coin in coins:
        if i - coin >= 0:
            dp[i] = min(dp[i], dp[i-coin] + 1)
if dp[-1] == 10001:
    print(-1)
else:
    print(dp[-1])
