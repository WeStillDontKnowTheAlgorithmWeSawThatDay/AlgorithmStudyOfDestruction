# 효율성 통과 어떻게 함????? 개어렵네

def solution(info, query):
    answer = []

    db = []
    for x in info :
        db.append(list(x.split(" ")))


    for xx in query :
        l = list(xx.split(" "))
        s = {'and'}
        l = [i for i in l if i not in s]

        ll = db
        if l[0] != '-' :
            ll = [a for a in ll if a[0] == l[0]]
        if l[1] != '-' :
            ll = [b for b in ll if b[1] == l[1]]
        if l[2] != '-' :
            ll = [c for c in ll if c[2] == l[2]]
        if l[3] != '-' :
            ll = [d for d in ll if d[3] == l[3]]
        ll = [e for e in ll if int(e[4]) >= int(l[4])]

        answer.append(len(ll))
    return answer
