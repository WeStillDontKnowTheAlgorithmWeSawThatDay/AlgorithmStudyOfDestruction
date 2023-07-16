# **, 알고리즘 생각해내기 어려웠다
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]
coins.sort()

dp = [0]*(k+1)
for i in range(0, k+1):
    if i % coins[0] == 0:
        dp[i] = 1

if len(coins) == 1:
    print(dp[k])

else:
    for coin in coins[1:]:
        for i in range(k+1):
            if i-coin >= 0:
                dp[i] += dp[i-coin]

    print(dp[k])

''' 
# 시간초과 풀이 (재귀함수) 
# top-down
def func(pos, remain, sum):
    if pos == len(coins) or remain < 0:
        return sum
    coin = coins[pos]
    quotient = remain // coin
    for i in range(quotient, -1, -1):
        if coin * i == remain:
            sum += 1
            if pos == len(coins) - 1:
                break
        elif coin * i < remain:
            sum = func(pos+1, remain - (coin*i), sum)
    return sum

import sys
input = sys.stdin.readline

n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]
coins.sort(reverse=True)

print(func(0, k, 0))
'''
