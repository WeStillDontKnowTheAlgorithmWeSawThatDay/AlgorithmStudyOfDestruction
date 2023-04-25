def convert(num):
    if num % 2 == 0:
        return num // 2
    else:
        return num * 3 + 1


def solution(num):
    answer = 0
    for i in range(501):
        if i == 500:
            return -1
        if num == 1:
            break
        num = convert(num)
        answer += 1

    return answer