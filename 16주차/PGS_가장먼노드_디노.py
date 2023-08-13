from collections import deque


def solution(n, edge):
    answer = 0
    arr = [[] for _ in range(n + 1)]
    dt = [-1] * (n + 1)

    for e in edge:
        arr[e[0]].append(e[1])
        arr[e[1]].append(e[0])

    dq = deque([1])
    dt[1] = 0

    while dq:
        now = dq.popleft()

        for i in arr[now]:
            if dt[i] == -1:
                dq.append(i)
                dt[i] = dt[now] + 1
    for d in dt:
        if d == max(dt):
            answer += 1
    return answer
