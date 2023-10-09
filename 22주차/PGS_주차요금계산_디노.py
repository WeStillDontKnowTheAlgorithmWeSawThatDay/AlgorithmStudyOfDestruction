from math import ceil


def solution(fees, records):
    answer = []

    dic = {}

    for r in records:
        time, number, io = r.split()
        h, m = map(int, time.split(':'))
        tmp = h * 60 + m

        if number in dic:
            dic[number].append([tmp, io])
        else:
            dic[number] = [[tmp, io]]
        # print(dic)

    car_list = list(dic.items())
    car_list.sort(key=lambda x: x[0])

    for cars in car_list:
        time = 0
        stack = []

        for car in cars[1]:
            if car[1] == 'IN':
                stack.append(car[0])
            else:
                time += car[0] - stack.pop()

        if len(stack) != 0:
            time += 1439 - stack.pop()

        if time <= fees[0]:
            answer.append(fees[1])
        else:
            answer.append(fees[1] + ceil((time - fees[0]) / fees[2]) * fees[3])

    return answer
