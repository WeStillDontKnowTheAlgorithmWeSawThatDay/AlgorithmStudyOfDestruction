def solution(numbers):
    answer = ''

    str_numbers = [str(n) for n in numbers]

    #     for n in numbers:
    #         str_numbers.append(str(n) * 3)

    #     print(str_numbers)

    str_numbers.sort(key=lambda x: x * 3, reverse=True)
    # print(str_numbers)

    answer = str(int(''.join(str_numbers)))

    return answer
