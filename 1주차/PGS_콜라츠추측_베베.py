def solution(num):
    if num == 1:
        return 0
    i = 0
    while num != 1:
        if i == 500:
            return -1
        elif num % 2 == 0:
            num = isEven(num)
        else:
            num = isOdd(num)
        i += 1
    return i

def isEven(num):
    return num / 2

def isOdd(num):
    return (num * 3) + 1