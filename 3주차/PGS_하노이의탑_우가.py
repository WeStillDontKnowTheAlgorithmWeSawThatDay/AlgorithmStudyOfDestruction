def solution(n):
    answer = []
    
    def move(n, start, des, temp):
        a=[]
        if(n == 1):
            a.append(start)
            a.append(des)
            answer.append(a)
            return
        move(n - 1, start, temp, des)
        a.append(start)
        a.append(des)
        answer.append(a)
        move(n - 1, temp, des, start)
    move(n, 1, 3, 2)
    return answer
