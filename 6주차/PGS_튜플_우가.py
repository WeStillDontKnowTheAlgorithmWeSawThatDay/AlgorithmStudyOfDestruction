def solution(s):
    answer = []
    s = s[2:-2]
    s = s.split("},{")
    s.sort(key=lambda x : len(x))
    
    for ss in s:
        for k in ss.split(","):
            if int(k) not in answer:
                answer.append(int(k))
    
    return answer
