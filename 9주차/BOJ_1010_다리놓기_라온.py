# *
# nCr = n-1Cr-1 + n-1Cr

dp = [[-1 for _ in range(30)] for _ in range(30)]
def func(n, r):
    if r == 0:
        return 1
    if n == r:
        return 1
    if dp[n-1][r-1] == -1:
        dp[n-1][r-1] = func(n-1, r-1)
    if dp[n-1][r] == -1:
        dp[n-1][r] = func(n-1, r)
    return dp[n-1][r-1] + dp[n-1][r]

T = int(input())

for _ in range(T):
    n, m = map(int, input().split())
    print(func(m, n))
