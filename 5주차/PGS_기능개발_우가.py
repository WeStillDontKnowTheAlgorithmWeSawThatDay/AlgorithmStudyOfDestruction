from collections import deque
import math

def solution(progresses, speeds):
    have = []
    dq = deque()
    
    for prog in progresses:
        have.append(100 - int(prog))
    
    for spd in range(len(speeds)):
        day = math.ceil(have[spd] / speeds[spd])
        dq.append(int(day))
    
    answer = []
    count = 1
    a = dq.popleft()
    while dq:
        b = dq.popleft()
        if a < b:
            a = b
            answer.append(count)
            count = 1
            continue
        else:
            count += 1
    if sum(answer) != len(speeds):
        answer.append(count)
    
    return answer
