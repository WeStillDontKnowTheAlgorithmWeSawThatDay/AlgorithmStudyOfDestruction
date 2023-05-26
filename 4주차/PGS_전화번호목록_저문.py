def solution(numbers):
    for number in numbers:
        for i in numbers:
            if i is not number and i.startswith(number):
                return False
    return True