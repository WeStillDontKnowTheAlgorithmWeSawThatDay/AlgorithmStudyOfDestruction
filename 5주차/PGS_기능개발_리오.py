import math

def solution(progresses, speeds):
    i = 0
    l = []
    answer = []

    for i in range(len(progresses)) :
        l.append(math.ceil((100 - progresses[i]) / speeds[i]))

    a = l[0]
    idx = 0
    c = 1

    for ii in range(1, len(l)) :
        if len(l) == 1 :
            answer.append(1)
            break

        if l[ii] > a :
            idx = ii
            answer.append(c)
            a = l[ii]
            c = 1
        else :
            c += 1


        if ii == len(l) - 1:
            answer.append(c)
            break
    return answer
