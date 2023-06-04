def solution(s):
    answer = []

    s = s[2:-2]
    s = s.split("},{")

    for i in s:
        answer.append(i.split(','))

    answer.sort(key=len)

    real = []
    for i in answer:
        for j in i:
            if int(j) not in real:
                real.append(int(j))

    return real