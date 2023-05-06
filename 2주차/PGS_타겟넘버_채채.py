def solution(numbers, target):
    answer = 0
    parents = [0]
    for number in numbers:
        newParents = []
        for parent in parents:
            newParents.append(parent + number)
            newParents.append(parent - number)
        parents = newParents
        print(parents)

    for parent in parents:
        if(parent == target):
            answer +=1
            
    return answer
