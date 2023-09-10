# 유니온파인드 정리 필요

import sys

sys.setrecursionlimit(10 ** 4)


def find_parent(table, x):
    # print(table)
    if x not in table:
        table[x] = x
        return x
    if table[x] == x:
        return x
    table[x] = find_parent(table, table[x])
    return table[x]


def solution(k, room_number):
    result = []
    dic = {}
    for room in room_number:
        chkRoom = find_parent(dic, room)
        # print(chkRoom)
        result.append(chkRoom)
        dic[chkRoom] = chkRoom + 1
        # print(dic[chkRoom])
    return result









def solution(k, room_number):
    answer = []
    dic = {}

    for room in room_number:
        n = room
        visit = [n]
        while n in dic:
            n = dic[n]
            visit.append(n)
        answer.append(n)
        for j in visit:
            dic[j] = n + 1

    return answer
