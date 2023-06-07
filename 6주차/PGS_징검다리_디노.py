def solution(distance, rocks, n):
    answer = 0
    rocks.sort()
    st, end = 0, distance

    while st <= end:
        mid = (st + end) // 2
        # print(mid)
        now, cnt = 0, 0

        for r in rocks:
            if r - now < mid:
                cnt += 1
            else:
                now = r

        if distance - now < mid:
            cnt += 1

        if cnt <= n:
            st = mid + 1
            answer = mid
            continue

        end = mid - 1
        # print(st, end)

    return answer