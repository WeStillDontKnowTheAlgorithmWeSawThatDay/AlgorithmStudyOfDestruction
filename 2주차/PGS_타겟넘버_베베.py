def solution(numbers, target):
    answer = 0

    def dfs(index, total):
        nonlocal answer
        if index == len(numbers):
            if total == target:
                answer += 1
            return
        dfs(index + 1, total + numbers[index])
        dfs(index + 1, total - numbers[index])

    dfs(0, 0)
    return answer
