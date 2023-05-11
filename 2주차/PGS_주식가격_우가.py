def solution(prices):
    answer = []

    for i in range(0, len(prices)):
        count = 0
        for p in range(i + 1, len(prices)):
            if(prices[i] <= prices[p]):
                count += 1
            else:
                count += 1
                break

        answer.append(count)

    return answer


a = [1, 2, 3, 2, 3]
print(solution(a))