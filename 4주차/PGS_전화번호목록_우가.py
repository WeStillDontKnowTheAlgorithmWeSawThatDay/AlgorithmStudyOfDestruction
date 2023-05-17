def solution(입력값):
    dic = {}
    
    입력값.sort()

    for pb in 입력값:
        dic[pb] = 0
    
    for pb in range(1, len(입력값)):
        temp = ""
        for pbstr in 입력값[pb]:
            temp += pbstr
            if temp in dic and temp != 입력값[pb]:
                return False
        
    return True
