from itertools import combinations as cb
from collections import defaultdict as dd
from bisect import bisect_left as bl


def solution(info, query):
    dic = dd(list)
    answer = []
    for ii in info:
        언어, 직군, 경력, 푸드, 코테 = ii.split()
        # print(언어, 직군, 경력, 푸드, 코테)

        for i in range(5):
            for k in cb([언어, 직군, 경력, 푸드], i):
                # print(k)
                # print("".join(k))
                # dic[k].append(코테)
                dic["".join(k)].append(int(코테))
    # print(dic)

    for d in dic:
        dic[d].sort()
    # print(dic)
    # for d in dic:
    #     print(d)

    for q in query:
        # print(":ds")
        qq = q.split()
        q_v = qq[-1]
        tmp = qq[:-1]

        q_list = []
        for t in tmp:
            if t != 'and' and t != '-':
                q_list.append(t)

        # print(q_list)
        # print("".join(q_list))
        k = "".join(q_list)
        # print(k)
        if k in dic:
            s_list = dic[k]

            if s_list:
                answer.append(len(s_list) - bl(s_list, int(q_v)))
                # print(len(s_list) - bl(s_list, int(q_v)))
                continue

        answer.append(0)

    return answer
