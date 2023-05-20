from collections import defaultdict

def solution(id_list, report, k):
    answer = []
    report = list(set(report))
    user = defaultdict(set)
    cnt = defaultdict(int)
    
    for r in report:
        a,b = r.split(' ')
        user[a].add(b)
        cnt[b] += 1

    for id in id_list:
        result = 0
        for u in user[id]:
            if cnt[u]>=k:
                result +=1
        answer.append(result)
    return answer

    
    
