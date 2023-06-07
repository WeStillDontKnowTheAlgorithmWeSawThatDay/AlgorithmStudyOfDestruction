from itertools import combinations

def solution(distance, rocks, n):
    rocks.sort()
    rocks.append(distance)

    low = 1
    high = distance

    answer = 0

    while low <= high:
        mid = (low + high) // 2
        현재바위 = 0
        count = 0
        for i in range(len(rocks)):
            다음바위 = rocks[i]

            if 다음바위 - 현재바위 < mid:
                count += 1

            else:
                현재바위 = 다음바위

            if n < count:
                break

        if count <= n:
            answer = mid
            low = mid + 1

        else:
            high = mid - 1

    return answer
