def solution(N, number):
    dp = [set() for i in range(9)]
    
    for i in range(1, 9):
        dp[i].add(int(str(N)*i))
        for j in range(i//2 + 1):
            for first in dp[j]:
                for second in dp[i-j]:
                    dp[i].add(first + second)
                    dp[i].add(first - second)
                    dp[i].add(second - first)
                    dp[i].add(first * second)
                    if second != 0 :
                        dp[i].add(first // second)
                    if first != 0 :
                        dp[i].add(second // first)
                    
        if number in dp[i]:
            return i

    return answer