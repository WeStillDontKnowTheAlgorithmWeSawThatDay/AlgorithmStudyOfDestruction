def solution(n, times):
    answer = 0
    st, end = min(times), max(times) * n

    while st <= end:
        m = (st + end) // 2
        cnt = 0

        for t in times:
            cnt += m // t

        if cnt >= n:
            answer = m
            end = m - 1
        else:
            st = m + 1

    return answer
