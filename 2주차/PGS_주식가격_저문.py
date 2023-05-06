def solution(prices):
    answer = [0] * len(prices)

    for i in range(len(prices)):
        for j in range(i, len(prices) - 1):
            if prices[i] <= prices[j]:
                answer[i] += 1
            else:
                break

    return answer
