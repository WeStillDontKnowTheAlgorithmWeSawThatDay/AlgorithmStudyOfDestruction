N = int(input())
period = [0]
cost = [0]
dp = [0 for _ in range(N + 2)]

for _ in range(N):
    t, p = map(int, input().split())
    period.append(t)
    cost.append(p)

# print(period)
# print(cost)
# print(dp)

for i in range(1, N + 1):
    print("i = ", i)
    if i + period[i] <= N + 1:
        for j in range(i + period[i], N+2):
            dp[j] = max(dp[j], dp[i] + cost[i])
    print(dp)

print(dp[N+1])
