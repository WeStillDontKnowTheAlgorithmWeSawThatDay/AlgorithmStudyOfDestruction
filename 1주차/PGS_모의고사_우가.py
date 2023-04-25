def solution(answers):
    answer = []
    student1 = [1,2,3,4,5]
    student2 = [2,1,2,3,2,4,2,5]
    student3 = [3,3,1,1,2,2,4,4,5,5]

    count1 = 0
    count2 = 0
    count3 = 0
    for idx, val in enumerate(answers):
        if(student1[idx % 5] == val):
            count1 += 1
        if(student2[idx % 8] == val):
            count2 += 1
        if(student3[idx % 10] == val):
            count3 += 1
    maxCount = max(count1, count2, count3)
    if(maxCount == count1):
        answer.append(1)
    if(maxCount == count2):
        answer.append(2)
    if(maxCount == count3):
        answer.append(3)

    return answer