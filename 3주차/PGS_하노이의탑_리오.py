def solution(n):
    answer = hanoi(n, 1, 2, 3)
    return answer

def hanoi(n, start, mid, end):
    l = []
    if n == 1 :
        l.append([start, end])
        return l
    else :
        l += hanoi(n-1, start, end, mid)
        l.append([start, end])
        l += hanoi(n-1, mid, start, end)
        return l

