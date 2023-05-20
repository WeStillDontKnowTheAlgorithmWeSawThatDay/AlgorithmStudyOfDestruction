def solution(s):
    answer = ''
    words = s.split(' ')
    for word in words:
        for i in range(len(word)):
            if i % 2 == 0:
                answer += word[i].upper()
            else:
                answer += word[i].lower()
        answer += ' '
    return answer[:-1]
