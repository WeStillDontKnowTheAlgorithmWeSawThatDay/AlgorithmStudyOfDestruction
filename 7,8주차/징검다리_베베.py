def solution(distance, rocks, n):
    rocks.sort()

    left = 1
    right = distance
    answer = 0

    while left <= right:
        mid = (left + right) // 2
        removedRock = 0
        before = 0

        for rock in rocks:
            if rock - before < mid:
                removedRock += 1
                continue

            before = rock

        if distance - before < mid:
            removedRock += 1

        if removedRock > n:
            right = mid - 1
            continue

        answer = max(answer, mid)
        left = mid + 1

    return answer
