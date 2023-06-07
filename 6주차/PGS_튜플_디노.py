def solution(s):
    answer = []
    l = list(s.split("{"))
    lll = []
    for ll in l:
        l3 = list(ll.split("}"))
        for l4 in l3:
            if l4 != '' and l4 != ',':
                lll.append(l4)

    # print(lll)
    dic = {}
    for llll in lll:
        tmp = list(llll.split(","))
        for t in tmp:
            if t not in dic:
                dic[t] = 1
            else:
                dic[t] += 1

    # for d in dic:
    #     answer.append(int(d))
    for i in range(len(dic), 0, -1):
        for d in dic:
            if dic[d] == i:
                answer.append(int(d))
    # print(dic)

    return answer