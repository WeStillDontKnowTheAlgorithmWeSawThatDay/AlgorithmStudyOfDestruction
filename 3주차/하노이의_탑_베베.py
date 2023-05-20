def solution(n):
    answer = []

    def hanoi(n, start, end, aux):
        if n == 1:
            answer.append([start, end])
        else:
            hanoi(n - 1, start, aux, end)
            answer.append([start, end])
            hanoi(n - 1, aux, end, start)

    hanoi(n, 1, 3, 2)

    return answer
