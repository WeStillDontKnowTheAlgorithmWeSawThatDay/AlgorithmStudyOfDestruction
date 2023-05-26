import math
def solution(brown, yellow):
    answer = []
    block = brown + yellow
    if math.sqrt(yellow)%1.0 == 0.0 and math.sqrt(block)%1.0 == 0.0: # 제곱승인지 확인
        return [int(math.sqrt(block)), int(math.sqrt(block))]
    
    i = 3
    while(i*3 <= block):
        j = 3
        while (i*j <= block):
            if i*j == block and (i-2)*(j-2) == yellow:
                return [max(i, j), min(i, j)]
            j += 1
        i += 1
    return answer
