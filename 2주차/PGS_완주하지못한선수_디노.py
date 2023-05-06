def solution(participant, completion):
    par_dic = {}

    for p in participant:
        par_dic[p] = par_dic.get(p, 0) + 1

    for c in completion:
        par_dic[c] -= 1

    for pd in par_dic:
        if par_dic[pd] == 1:
            return pd

    # return next(k for k, v in par_dic.items() if par_dic[k] == 1)
