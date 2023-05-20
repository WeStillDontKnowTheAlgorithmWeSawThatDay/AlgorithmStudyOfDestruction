def solution(N, number):
    answer = 0
    
    if N == number:
        return 1;
    
    temp = []
    temp.append(set())
    temp.append(set())
    temp.append(set())
    temp.append(set())
    temp.append(set())
    temp.append(set())
    temp.append(set())
    temp.append(set())
    temp.append(set())
    
    
    # 1. 1 ~ 9 까지 돈다
    for i in range(1, 9):
        temps = temp[i]
        strTemp = str(N)
        temps.add(int(strTemp * i))
        
        for j in range(1, i):
            for k in temp[j]:
                for l in temp[i - j]:
                    temps.add(k + l)
                    temps.add(k * l)
                    if k - l > 0:
                        temps.add(k - l)
                    if l != 0 and k != 0:
                        temps.add(k // l) 
                        
        if number in temps:
            return i
    
    return -1
