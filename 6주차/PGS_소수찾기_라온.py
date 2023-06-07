import itertools
import math

def solution(numbers):
    answer = 0
    numbers = list(numbers)
    
    cases = []
    for i in range(len(numbers)):
        for j in itertools.permutations(numbers, i+1):
            num = int(''.join(j))
            if (num%2 != 0 and num != 1 and num != 0) or num == 2:
                cases.append(num)

    cases = list(set(cases))
    for case in cases:
        if is_prime(case):
            answer += 1
    return answer

def is_prime(x):
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True
    