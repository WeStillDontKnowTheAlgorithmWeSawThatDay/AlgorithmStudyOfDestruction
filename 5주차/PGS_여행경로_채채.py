from collections import deque
from collections import defaultdict
def solution(tickets):
    answer = []
    tickets.sort(key = lambda x:(x[1], x[0]))
    for i, [start, end] in enumerate(tickets):
        if start == "ICN":
            first, end = tickets.pop(i)
            break
    q = deque([])
    q.append([first, end])
    answer.append(first)
    answer.append(end)
    while q:
        start, dest = q.popleft()
        for i, [s, d] in enumerate(tickets):
            if dest == s:
                begin, end = tickets.pop(i)
                q.append([begin, end])
                answer.append(end)
                break
     
    return answer
