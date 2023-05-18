def solution(brown, yellow):
    answer = []
    
    넓이 = brown + yellow
    
    for i in range(int(brown/2)):
        for j in range(int(brown/2)):
            if i < j:
                continue
            if i * j == 넓이 and ((i-2) * (j-2)) == yellow:
                answer.append(i)
                answer.append(j)
                return answer

    return answer
