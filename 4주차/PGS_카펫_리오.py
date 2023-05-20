def solution(brown, yellow):
    a = brown + yellow
    answer = []
    for i in range(1,a) :
        ii = a / i
        if int(ii) == ii and ((i + ii) * 2) - 4 == brown :
            answer.append(ii)
            answer.append(i)
            break
    return answer
