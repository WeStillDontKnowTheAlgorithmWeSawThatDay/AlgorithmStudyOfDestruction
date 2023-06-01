def solution(numbers):
    answer = []

    for n in numbers:
        bn = list('0' + bin(n)[2:])
        i = ''.join(bn).rfind('0')
        bn[i] = '1'

        if n % 2 == 1:
            bn[i+1] = '0'

        answer.append(int(''.join(bn), 2))

    return answer
