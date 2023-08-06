def solution(clothes):
    answer = 1
    dic = {}
    for c in clothes:
        if c[1] in dic:
            dic[c[1]] += 1
        else:
            dic[c[1]] = 1
    # print(dic)

    for d in dic:
        answer *= (dic[d] + 1)
        # print(answer)

    return answer - 1
