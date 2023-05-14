def solution(citations):
    answer = 0
    
    if len(citations) == 1:
        return 1   
    # h == 3 이면
    # 3 이상 3개
    # 3 이하 3개
    
    # 역으로 정렬을 했을 경우에, 인덱스가 최대 인용 수 보다 크면 return
    citations.sort(reverse=True)
    

    for i in range(len(citations)):
        
        # 조건 만족 o
        if i >= citations[i]:
            return i
        
    # 반복문 돌면서 조건 다 안되면? 그냥 배열 길이가 정답
    return len(citations)
