def solution(s):
    c = 0
    answer = ''
    for x in list(s) :

        if x == " " :
            answer += " "
            c = 0
            continue

        c += 1
        if (c % 2 == 0) :
            answer += x.lower()
            continue
        answer += x.upper()

    return answer
