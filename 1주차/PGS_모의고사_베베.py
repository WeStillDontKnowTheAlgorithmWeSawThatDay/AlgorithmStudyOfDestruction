def solution(answers: list):
    pattern1 = [1, 2, 3, 4, 5]
    pattern2 = [2, 1, 2, 3, 2, 4, 2, 5]
    pattern3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    person1, person2, person3 = 0, 0, 0
    for i in range(len(answers)):
        s1 = i % 5
        s2 = i % 8
        s3 = i % 10

        if pattern1[s1] == answers[i]:
            person1 += 1
        if pattern2[s2] == answers[i]:
            person2 += 1
        if pattern3[s3] == answers[i]:
            person3 += 1

    k = max(person1, person2, person3)
    answer = []

    if k == person1:
        answer.append(1)
    if k == person2:
        answer.append(2)
    if k == person3:
        answer.append(3)

    return answer