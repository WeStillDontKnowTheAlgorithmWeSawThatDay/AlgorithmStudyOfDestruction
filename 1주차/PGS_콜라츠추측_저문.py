def solution(num):
    if num == 1:
        return 0

    count = 0
    while True:
        if num == 1:
            break
        if count == 500:
            return -1

        if num % 2 == 0:
            num /= 2
            count += 1
        elif num % 2 == 1:
            num = num * 3 + 1
            count += 1

    return count