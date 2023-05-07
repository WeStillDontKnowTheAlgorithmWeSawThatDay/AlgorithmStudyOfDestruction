def solution(n, times):
    left, right = 1, max(times) * n

    while left <= right:
        mid = (left + right) // 2
        count = 0

        for t in times:
            count += mid // t

            if count >= n:
                break

        if count >= n:
            right = mid - 1
        else:
            left = mid + 1

    return left
