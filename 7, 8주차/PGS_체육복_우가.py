def solution(n, lost, reserve):
    answer = 0
    
    for l in lost:
        if l in reserve:
            reserve.remove(l)
            lost.remove(l)
    
    for res in reserve:
        if len(lost) == 0:
            return n
        if res - 1 in lost:
            lost.remove(res - 1)
        elif res + 1 in lost:
            lost.remove(res + 1)

    return n - len(lost)
# 86.7점이 나오네요,,,,
