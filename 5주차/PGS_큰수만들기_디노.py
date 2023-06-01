def solution(number, k):
    answer = ''

    for n in number:
        while answer and k > 0 and answer[-1] < n:
            answer = answer[:len(answer) - 1]
            k -= 1
        answer += n

    return answer[:len(answer) - k]

# 테스트 12
# 54321, 2, 543