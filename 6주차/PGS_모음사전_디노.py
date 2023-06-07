def append_vo(li, vo):
    newTmp = []
    for l in li:
        tmp = []
        for v in vo:
            tmp.append(l + v)
        newTmp += tmp
    return newTmp


def solution(word):
    answer = 0
    vo = ['A', 'E', 'I', 'O', 'U']

    #     for v in vo:
    #         ansList.append(v)

    #     tmp = ""
    #     for i in range(2):
    #         for v in vo:
    #             tmp += v

    ansList = ['A', 'E', 'I', 'O', 'U']
    ansList2 = {}
    for _ in range(4):
        ansList += append_vo(ansList, vo)

    ansList.sort()

    for aa in ansList:
        if aa not in ansList2:
            ansList2[aa] = 1
    # print(ansList2)
    cnt = 1
    for aaa in ansList2:
        if aaa == word:
            return cnt
        cnt += 1
    # for i in range(len(ansList)):
    #     if word == ansList[i]:
    #         answer = i+1
    # return answer