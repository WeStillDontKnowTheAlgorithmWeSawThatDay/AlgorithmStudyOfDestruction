def solution(n):
    answer = []
    num = 0
    for i in range(1, n+1):
        num += i
    answer = [0 for _ in range(num)]
    
    start, end, temp = 0, n, 2
    index = 1
    
    j = 1
    while j <= num:
        for i in range(start, end):
            index += i
            answer[index-1] = j
            j += 1

        for i in range(n-1):
            index += 1
            answer[index-1] = j
            j += 1
            
        for i in range(end, temp, -1):
            index -= i
            answer[index-1] = j
            j += 1
        
        start = temp
        temp += 2
        n -= 3
        end -= 1

    return answer