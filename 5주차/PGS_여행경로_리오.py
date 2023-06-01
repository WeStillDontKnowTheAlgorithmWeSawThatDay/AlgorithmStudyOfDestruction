from collections import deque
def solution(tickets):
    answer = []
    q = deque()
    q.append(("ICN",["ICN"], []))

    while q:
        airport, path, used = q.popleft()

        if len(used) == len(tickets):
            answer.append(path)

        for idx, ticket in enumerate(tickets):
            if ticket[0] == airport and not idx in used:
                q.append((ticket[1], path+[ticket[1]], used+[idx]))


    answer.sort()

    return answer[0]
