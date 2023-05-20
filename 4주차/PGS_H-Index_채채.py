def solution(citations):
    citations = sorted(citations)
    # 0,1,3,5,6,7,8
    a = len(citations)
    for i in range(a):
        if citations[i] >= a-i:
            return a-i
    return 0
