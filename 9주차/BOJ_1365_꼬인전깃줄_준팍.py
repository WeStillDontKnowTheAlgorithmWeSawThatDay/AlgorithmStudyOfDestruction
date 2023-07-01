import sys
from bisect import bisect_left

input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

dp = [0]

for i in range(N):
    if dp[-1] < arr[i]:
        dp.append(arr[i])
    else:
        dp[bisect_left(dp, arr[i])] = arr[i]

print(N - len(dp) + 1)
