def solution(genres, plays):
    answer = []
    a = {}
    c = {}
    for genre in genres:
        a[genre] = []
        c[genre] = 0
    
    for i in range(len(plays)):
        c[genres[i]] += plays[i]
    
    b = {}
    for i in range(len(plays)):
        b[i] = plays[i]

    b = sorted(b.items(), key = lambda item: item[1], reverse = True)

    for bb in b:
        if len(a[genres[bb[0]]]) < 2:
            a[genres[bb[0]]].append(bb[0])
    
    c = sorted(c.items(), key = lambda item: item[1], reverse = True)

    for cc in c:
        for ans in a[cc[0]]:
            answer.append(ans)
    
    return answer
