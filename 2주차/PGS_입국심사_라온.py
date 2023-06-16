# 이분 탐색의 범위는 무엇으로 할지, 이분 탐색의 기준을 무엇으로 할지 

def solution(n, times):
    left, right = min(times), max(times) * n
    while left < right:
        people = 0
        mid = (left + right) // 2
        
        for time in times:
            people += (mid // time)
        
        if people >= n:
            right = mid
        
        if people < n:
            left = mid + 1
    return left