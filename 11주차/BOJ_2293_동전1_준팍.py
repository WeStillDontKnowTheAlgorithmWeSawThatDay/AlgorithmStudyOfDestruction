import sys

input = sys.stdin.readline

def countCoins(coins, k):
    dp = [0 for _ in range(k + 1)]
    dp[0] = 1 # 0원을 만드는 경우의 수는 1가지 (동전을 아예 사용하지 않는 경우)

    for coin in coins:
        for i in range(coin, k + 1):
            dp[i] += dp[i - coin]

    return dp[k]

n, k = map(int, input().split())

coins = [int(input()) for _ in range(n)]

print(countCoins(coins, k))
