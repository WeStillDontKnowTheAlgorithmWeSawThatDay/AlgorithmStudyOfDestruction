def solution(n):
    temp1 = 0
    temp2 = 1
    for i in range(n + 1):
        if i == 0:
            temp3 = 0
        elif i == 1:
            temp3 = 1
        else:
            temp3 = temp1 + temp2
            temp1 = temp2
            temp2 = temp3

    return temp3 % 1234567
