from collections import deque

def solution(tickets):
    answer = []
    
    checked = {}
    for start, end in tickets:
        if start not in checked:
            checked[start] = []
        checked[start].append(end)
    
    for key in checked.keys():
        checked[key].sort()
    
    dq = ['ICN']
    path = []
    
    while dq:
        now = dq[-1]
        
        if now not in checked or len(checked[now]) == 0:
            path.append(dq.pop())
        else:
            nexts = checked[now].pop(0)
            dq.append(nexts)
    
    answer = path[::-1]
    
    return answer
