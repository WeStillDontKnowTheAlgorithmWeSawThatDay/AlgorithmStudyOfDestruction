def solution(n, lost, reserve):
    answer = 0
    
    lost.sort()
    reserve.sort()
    
    temp = []
    for l in lost:
        if l in reserve:
            reserve.remove(l)
            temp.append(l)
    
    for te in temp:
        lost.remove(te)
    
    for res in reserve:
        if len(lost) == 0:
            return n
        if res - 1 in lost:
            lost.remove(res - 1)
        elif res + 1 in lost:
            lost.remove(res + 1)

    return n - len(lost)
