def solution(id_list, report, k):
    answer = []
    dic = {}
    
    for id in id_list:
        dic[id] = set({})

    
    for repo in report:
        신고자, 신고당한자 = repo.split(" ")
        dic[신고자].add(신고당한자)

    di = dict.fromkeys(id_list, 0)
    
    diccc = dict.fromkeys(id_list, 0)
    
    for dd in dic:
        for did in dic[dd]:
            di[did] += 1
            
    for dii in di:
        if di[dii] >= k:
            answer.append(dii)
    
    an = []

    for ddiicc in dic:
        count = 0
        for anss in answer:
            if anss in dic[ddiicc]:
                count += 1
        an.append(count)
    
    return an
