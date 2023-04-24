def solution(answers):
    answer = []

    p1 = [1, 2, 3, 4, 5] * len(answers)
    p2 = [2, 1, 2, 3, 2, 4, 2, 5] * len(answers)
    p3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * len(answers)

    answer_count = [0, 0, 0]

    for i in range(len(answers)):
        if p1[i] == answers[i]:
            answer_count[0] += 1
        if p2[i] == answers[i]:
            answer_count[1] += 1
        if p3[i] == answers[i]:
            answer_count[2] += 1

    for i in range(len(answer_count)):
        if answer_count[i] == max(answer_count):
            answer.append(i + 1)

    return answer