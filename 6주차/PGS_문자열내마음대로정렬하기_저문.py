def solution(words, n):
    answer = []
    order = {}

    for i in range(len(words)):
        words[i] = words[i][n] + words[i]

    words.sort()

    for word in words:
        answer.append(word[1:])

    return answer