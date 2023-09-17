def solution(s):
    answer = len(s)

    for i in range(1, len(s)):
        tmp = ""
        word = s[0:i]
        # print(word)
        cnt = 1

        for j in range(i, len(s), i):
            if word == s[j:j + i]:
                cnt += 1
                continue

            if cnt >= 2:
                tmp += str(cnt) + word
            else:
                tmp += word

            word = s[j:j + i]
            cnt = 1

        if cnt >= 2:
            tmp += str(cnt) + word
        else:
            tmp += word
        # print(tmp)
        answer = min(answer, len(tmp))

    return answer
