def solution(name):
    target = "A" + name
    answer = 0
    
    for i in range(len(target)-1):
        print (target[i])
        # 음수이면 오른쪽으로 이동
        if(ord(target[i]) - ord(target[i+1])<0):
            first = abs(ord(target[i+1]) - ord('Z'))+1
            
            second = abs(ord(target[i]) - ord(target[i+1]))
            answer += min(first,second)
        elif(ord(target[i]) - ord(target[i+1])>0):
            first = abs(ord(target[i+1]) - ord('A'))+1
            second = abs(ord(target[i]) - ord(target[i+1]))
            answer += min(first,second)
        else:
            answer += 0

    return answer
