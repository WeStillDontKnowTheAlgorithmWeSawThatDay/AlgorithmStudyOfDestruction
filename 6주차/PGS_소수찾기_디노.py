from itertools import permutations
def isPrime(x):
    if x < 2:
        return False
    # print(x)
    for i in range(2, x):
        if x % i == 0:
            return False
    return True


def solution(numbers):
    answer = 0
    nums = []

    for i in range(1, len(numbers) + 1):
        nums.append(list(set(map(''.join, permutations(numbers, i)))))
    per = list(set(map(int, set(sum(nums, [])))))

    for p in per:
        if isPrime(p):
            answer += 1

    return answer

# def solution(n):
#     a = set()
#     for i in range(len(n)):
#         a |= set(map(int, map("".join, permutations(list(n), i + 1))))
#     a -= set(range(0, 2))
#
#     for i in range(2, int(max(a) ** 0.5) + 1):
#         a -= set(range(i * 2, max(a) + 1, i))
#
#     return len(a)
