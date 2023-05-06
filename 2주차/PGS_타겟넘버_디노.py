def solution(numbers, target):
    answer = 0
    ansList = [0]
    for num in numbers:
        tmpList = []
        for a in ansList:
            tmpList.append(a + num)
            tmpList.append(a - num)
        ansList = tmpList
    for a in ansList:
        if a == target:
            answer += 1
    return answer
