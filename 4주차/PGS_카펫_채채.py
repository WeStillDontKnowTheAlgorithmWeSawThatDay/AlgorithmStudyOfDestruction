def solution(brown, yellow):
    answer = []
    for i in range(1,yellow+1):
        if(yellow% i == 0): 
            a = i
            b = yellow//i
            if(((a + 2) * 2 + (b * 2)) == brown) and (a>=b):
                answer.append(a+2)
                answer.append(b+2)
                break

    return answer
