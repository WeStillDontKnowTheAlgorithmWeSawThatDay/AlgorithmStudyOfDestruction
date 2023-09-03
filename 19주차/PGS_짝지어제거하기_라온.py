from collections import deque

def solution(s):
    answer = 0
    s = list(s)
    queue = deque()
    idx = 0
    while idx < len(s):
        if not queue:
            queue.append(s[idx])
            idx += 1
            continue
            
        if queue[-1] == s[idx]:
            queue.pop()
        else:
            queue.append(s[idx])
        idx += 1
    if len(queue) == 0:
        answer = 1
    return answer

# 시간초과 코드
def solution(s):
    answer = 0
    s = list(s)
    before = 0
    
    while len(s) and before < len(s) - 1:
        curr = before + 1
        if s[before] == s[curr]:
            s[before:] = s[curr+1:]
            if before > 0:
                before -= 1
        else:
            before += 1
    if len(s) == 0:
        answer = 1
    return answer