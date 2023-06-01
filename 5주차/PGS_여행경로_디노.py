from collections import deque
import copy

answer = []


def dfs(route, dic, limit):
    global answer
    if len(route) == limit + 1:
        answer.append(route)
        return

    now = route[-1]
    # print(now, dic[now])
    if now in dic:
        for i in range(len(dic[now])):
            # print(dic[now])
            tmp = copy.deepcopy(route)
            dic2 = copy.deepcopy(dic)
            dic2[now].pop(i)
            tmp.append(dic[now][i])
            dfs(tmp, dic2, limit)


def solution(tickets):
    dic = {}
    for t in tickets:
        fr, to = t[0], t[1]
        if fr in dic:
            dic[fr].append(to)
            # tmp = list(dic[fr])
            # tmp.sort()
            # dic[fr] = deque(tmp)
        else:
            # dic[fr] = deque([to])
            dic[fr] = [to]
            # print(dic)

    # print(dic)
    # answer.append('ICN')

    # for _ in range(len(tickets)):
    #     now = answer[-1]
    #     answer.append(dic[now][0])
    #     dic[now].popleft()

    dfs(['ICN'], dic, len(tickets))

    # print(answer)
    return min(answer)