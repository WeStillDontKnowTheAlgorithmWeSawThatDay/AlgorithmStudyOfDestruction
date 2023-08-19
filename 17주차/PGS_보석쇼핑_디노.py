def solution(gems):
    answer = [1, len(gems)]
    dic = {}
    for g in gems:
        if g not in dic:
            dic[g] = 1
    gemNum = len(dic)
    le, ri = 0, 0

    my_gem = {}
    min_len = len(gems)

    while ri < len(gems):
        if gems[ri] not in my_gem:
            my_gem[gems[ri]] = 1
        else:
            my_gem[gems[ri]] += 1
        ri += 1

        if len(my_gem) == gemNum:
            while le < ri:
                if my_gem[gems[le]] > 1:
                    my_gem[gems[le]] -= 1
                    le += 1
                    continue
                if min_len > ri - le:
                    min_len = ri - le
                    answer = [le + 1, ri]

                break

    return answer
