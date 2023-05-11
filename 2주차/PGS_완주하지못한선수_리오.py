def solution(participant, completion):
    d = dict()
    for x in participant :
        if x in d :
            d[x] += 1
            continue
        d[x] = 1
    for y in completion :
        d[y] -= 1
    answer = ""
    for z in d :
        if d[z] != 0 :
            answer = z
    return answer
