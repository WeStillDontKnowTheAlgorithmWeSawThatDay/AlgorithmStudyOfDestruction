def solution(N, number):
    if number == N:
        return 1

    dp = [{int(str(N) * x)} for x in range(1, 9)]
    # print(dp)

    for i in range(8):
        for j in range(i):
            for d in dp[j]:
                # print(d)
                for p in dp[i - (j + 1)]:
                    dp[i].add(d + p)
                    dp[i].add(d - p)
                    dp[i].add(d * p)
                    if p != 0:
                        dp[i].add(d // p)

    for i in range(8):
        if number in dp[i]:
            return i + 1

    return -1
