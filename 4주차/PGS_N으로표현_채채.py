def funct(N,cnt):
    a = N
    for i in range(cnt-1):
        N = ((N*10)+a)
    return N

def solution(N, number):
    if(N == number):
        return 1
    
    answer = 0

    cnt = 2
    
    l = []
    l.append(0)
    l.append(1)
    l.append(2*N)
    l.append(N*N)
    l.append(funct(N,cnt))

    while(True):
        if(cnt>8):
            answer = -1
            break
        if number in l:
            answer = cnt
            break

        newList = set()
        cnt+=1
        for i in l:
            newList.add(i+N)
            newList.add(i-N)
            newList.add(i*N)
            if(N!=0):
                newList.add(i//N)
        newList.add(funct(N,cnt))     
        l = list(newList)
    

    return answer
print(solution(5,12))
