def solution(tickets):
    answer = []
    graph = {}

    for ticket in tickets:
        departure, arrival = ticket

        if departure in graph:
            graph[departure].append(arrival)
        else:
            graph[departure] = [arrival]

    for city in graph:
        graph[city].sort(reverse=True)

    stack = ['ICN']

    while stack:
        current = stack[-1]

        if current not in graph or len(graph[current]) == 0:
            answer.append(stack.pop())
        else:
            stack.append(graph[current].pop())

    answer.reverse()

    return answer
