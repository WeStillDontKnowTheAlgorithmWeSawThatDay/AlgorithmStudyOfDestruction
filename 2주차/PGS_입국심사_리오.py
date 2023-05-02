def solution(n, times):

    s, e = 0, max(times)*n
    answer = e

    while s <= e:
        m = (s + e) // 2

        p = 0
        for t in times:
            p += (m // t)

        if p < n:
            s = m + 1
        else:
            e = m - 1
            answer = min(answer, m)

    return answer
