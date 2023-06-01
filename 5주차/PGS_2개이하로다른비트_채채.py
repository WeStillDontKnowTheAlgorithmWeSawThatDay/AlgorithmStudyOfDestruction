def solution(numbers):
    answer = []
    for n in numbers:
        a = n^(n+1)
        if a < 4 :
            answer.append(n+1)
        else:
            a = a >> (2)
            answer.append(n+1+a)
    return answer
