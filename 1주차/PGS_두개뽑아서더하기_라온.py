def solution(numbers):
    answer = []
    for i in range(len(numbers)):
        for j in numbers[i+1:]:
            answer.append((numbers[i] + j))
    return sorted(list(set(answer)))