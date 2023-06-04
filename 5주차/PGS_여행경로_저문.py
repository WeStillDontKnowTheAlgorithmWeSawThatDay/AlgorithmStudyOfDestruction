def bfs(graph, start):
    visit = []
    queue = []
    queue.append(start)

    while queue:
        node = queue.pop(0)

        if node not in graph:
            visit.append(node)
            return visit

        if node not in visit:
            visit.append(node)
            queue.extend(graph[node])

    return visit


def solution(tickets):
    graph = {}

    for t in tickets:
        if t[0] not in graph:
            graph[t[0]] = {t[1]}
        else:
            graph[t[0]] = t[1]

    answer = bfs(graph, "ICN")

    return answer