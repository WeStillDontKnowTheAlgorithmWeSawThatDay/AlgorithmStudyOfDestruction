def solution(progresses, speeds):
    answer = []
    i, day = 0, 1
    temp = 0
    while(i < len(progresses)):
        work = speeds[i] * day
        if progresses[i] + work >= 100:
            i += 1
            if temp != day: 
                answer.append(1)
            else:   
                answer[len(answer)-1] += 1
            temp = day
        else:
            day += 1
    return answer