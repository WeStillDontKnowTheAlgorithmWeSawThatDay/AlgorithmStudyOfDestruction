def solution(id_list, report, k):
    dicw = dict()
    dica = dict()
    dicc = dict()
    for x in id_list :
        dicw[x] =  0
        dica[x] = []
        dicc[x] = 0
    for c in set(report) :
        a,b = c.split()
        dica[b].append(a)
        dicw[b] += 1
    for a,b in dicw.items() :
        if b >= k :
            for i in dica.get(a) :
                dicc[i] += 1

    answer = []
    for xx in id_list :
        answer.append(dicc.get(xx))
    return answer
