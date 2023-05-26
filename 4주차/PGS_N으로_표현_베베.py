def solution(N, number):
    dp = [set() for _ in range(9)]

    for i in range(1, 9):
        dp[i].add(int(str(N) * i))

        for j in range(1, i // 2 + 1):
            for x in dp[j]:
                for y in dp[i - j]:
                    dp[i].add(x + y)
                    dp[i].add(x - y)
                    dp[i].add(y - x)
                    dp[i].add(x * y)
                    if y != 0:
                        dp[i].add(x // y)
                    if x != 0:
                        dp[i].add(y // x)

        if number in dp[i]:
            return i

    return -1
