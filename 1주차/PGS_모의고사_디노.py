def solution(answers):
    answer = []
    one = [1, 2, 3, 4, 5]
    two = [2, 1, 2, 3, 2, 4, 2, 5]
    three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    cnt_1, cnt_2, cnt_3 = 0, 0, 0

    for i in range(len(answers)):
        if one[i % 5] == answers[i]:
            cnt_1 += 1
        if two[i % 8] == answers[i]:
            cnt_2 += 1
        if three[i % 10] == answers[i]:
            cnt_3 += 1

    max_cnt = max([cnt_1, cnt_2, cnt_3])

    if cnt_1 == max_cnt:
        answer.append(1)
    if cnt_2 == max_cnt:
        answer.append(2)
    if cnt_3 == max_cnt:
        answer.append(3)

    return answer
