from itertools import permutations
import math


def solution(n, k):
    answer = []

    arr = [i for i in range(1, n + 1)]

    while arr:
        a = (k - 1) // math.factorial(n - 1)
        answer.append(arr.pop(a))

        k %= math.factorial(n - 1)
        n -= 1

    return answer
