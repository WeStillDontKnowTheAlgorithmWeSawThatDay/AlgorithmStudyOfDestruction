# 이분탐색을 어떻게 적용해야하는지 감이 아예 안왔어요
# 이분 탐색의 범위는 무엇으로 할지, 이분 탐색의 기준을 무엇으로 할지 

def solution(n, times):
    answer = 0
    left, right = 1, max(times)*n
    while left < right:
        person = 0
        mid = (left + right) // 2
        for time in times:
            # mid분 동안 각 입국심사대에서 처리할 수 있는 인원 수
            # ex) [7, 10] => 33//7 + 33//10 = 7
            person += mid // time
        
        if person >= n:
            right = mid
            
        elif person < n:
            left = mid + 1
    return left