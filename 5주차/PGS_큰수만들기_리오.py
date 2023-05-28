def solution(number, k):
    l = []

    for (i, n) in enumerate(number):
        while l and l[-1] < n and k > 0:
            l.pop()
            k -= 1

        if k == 0:
            l += number[i:]
            break

        l.append(n)

    if k > 0 :
        l = l[:-k]

    answer = "".join(l)
    return answer
