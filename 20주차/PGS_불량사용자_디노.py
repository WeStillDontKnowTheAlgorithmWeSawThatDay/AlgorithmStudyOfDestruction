# 나 이문제 싫어

from itertools import combinations


def nCm(n, m):
    if m == 0 or n == 0:
        return 1
    num = 1
    for i in range(n, n - m, -1):
        num *= i
    for i in range(1, m + 1):
        num //= i
    return num


def is_match(banned, user):
    for b, u in zip(banned, user):
        if b != '*' and b != u:
            return False
    return True


def solution(user_id, banned_id):
    answer = 0
    banned_combinations = []

    for banned in banned_id:
        tmp_combinations = []

        for user in user_id:
            if len(user) != len(banned):
                continue
            if is_match(banned, user):
                tmp_combinations.append(user)

        banned_combinations.append(tmp_combinations)

    unique_combinations = set()

    def generate_combinations(index, current_combination):
        if index == len(banned_combinations):
            unique_combinations.add(tuple(sorted(current_combination)))
            return

        for user in banned_combinations[index]:
            if user not in current_combination:
                current_combination.append(user)
                generate_combinations(index + 1, current_combination)
                current_combination.pop()

    generate_combinations(0, [])

    for unique_combination in unique_combinations:
        answer += nCm(len(unique_combination), len(banned_id))

    return answer
