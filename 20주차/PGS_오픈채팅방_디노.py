def solution(record):
    answer = []

    dic = {}
    query = [list(r.split()) for r in record]

    # print(query)

    for q in query:
        if q[0] == "Enter" or q[0] == "Change":
            dic[q[1]] = q[2]

    for q in query:
        if q[0] == "Enter":
            answer.append(dic[q[1]] + "님이 들어왔습니다.")
        if q[0] == "Leave":
            answer.append(dic[q[1]] + "님이 나갔습니다.")

    return answer
