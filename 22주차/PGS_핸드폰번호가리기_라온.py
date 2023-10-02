def solution(phone_number):
    length = len(phone_number) - 4
    answer = "*"*length + phone_number[length:]
    return answer
