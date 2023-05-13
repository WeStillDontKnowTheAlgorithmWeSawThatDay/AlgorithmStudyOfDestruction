def solution(n, times):
    times.sort()
    answer = 0
    start = times[0]
    end = times[0] * n
    while True:
        count = 0
        mid = (start + end) // 2
        for i in times:
            count += (mid // i)
        if count >= n:
            end = mid
        elif count < n:
            start = mid
        if start > end - 1:
            answer = start
            break


    return answer
