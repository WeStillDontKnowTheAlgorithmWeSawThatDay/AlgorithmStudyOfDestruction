def solution(answers):
    a = [1,2,3,4,5] * 2000
    b = [2,1,2,3,2,4,2,5] * 1250
    c = [3,3,1,1,2,2,4,4,5,5] * 1000
    c_a = 0
    c_b = 0
    c_c = 0
    for i in range(len(answers)) :
        if answers[i] == a[i] :
            c_a += 1
        if answers[i] == b[i] :
            c_b += 1
        if answers[i] == c[i] :
            c_c += 1
    answer = []
    m = max(c_a, c_b, c_c)
    if m == c_a :
        answer.append(1)
    if m == c_b :
        answer.append(2)
    if m == c_c :
        answer.append(3)
    return answer
