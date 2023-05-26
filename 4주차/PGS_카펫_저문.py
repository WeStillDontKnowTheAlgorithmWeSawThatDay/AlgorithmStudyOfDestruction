def solution(brown, yellow):
    answer = []

    sum = brown + yellow
    divisors = []
    for i in range(1, sum + 1):
        if sum % i == 0:
            divisors.append(i)

    for divisor in divisors:
        across_divisor = sum / divisor
        if (across_divisor - 2) * (divisor - 2) == yellow:
            answer.append(across_divisor)
            answer.append(divisor)
            break

    return answer
