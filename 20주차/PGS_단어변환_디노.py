from collections import deque


def solution(begin, target, words):
    answer = 0
    word_len = len(words)

    dq = deque([[begin, 0, [begin]]])

    while dq:
        now, cnt, chk = dq.popleft()

        for i in range(len(words)):
            comp = words[i]
            if comp in chk:
                continue
            tmp_cnt = 0
            for j in range(len(comp)):
                if now[j] != comp[j]:
                    tmp_cnt += 1
            if tmp_cnt == 1:
                chk.append(comp)
                dq.append([comp, cnt + 1, chk])
                if comp == target:
                    return cnt + 1

    #     while stack:
    #         now = stack.pop()

    #         idx = 0
    #         while idx < len(words):
    #             cnt = 0
    #             for i in range(len(words[idx])):
    #                 if now[i] != words[idx][i]:
    #                     cnt += 1
    #             if cnt == 1:
    #                 stack.append(words[idx])
    #                 words.pop(idx)
    #                 if words[idx] == target:
    #                     return word_len - len(words)
    #                 continue
    #             idx += 1

    return answer
