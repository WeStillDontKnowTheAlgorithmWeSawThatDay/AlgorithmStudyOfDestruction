def hanoi(n, source, target, temp, move):
    if n == 1:
        move.append([source, target])
    else:
        hanoi(n - 1, source, temp, target, move)
        hanoi(1, source, target, temp, move)
        hanoi(n - 1, temp, target, source, move)


def solution(n):
    answer = []

    hanoi(n, 1, 3, 2, answer)

    return answer
