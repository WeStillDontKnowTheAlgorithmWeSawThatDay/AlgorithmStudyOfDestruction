from itertools import combinations

def solution(numbers, target):
    s = sum(numbers)
    d = int((s-target)/2)
    seta = set()
    answer = 0
    for i in range(len(numbers)+1) :
        l = combinations(numbers, i)
        for tu in l :
            if sum(tu) == d :
                answer += 1
    return answer
