def solution(words):
    answer = ''
    words = words.upper()
    i = 0
    for word in words:
        if word == " ":
            answer += " "
            i = 0
            continue
        if i%2 == 1:
            answer += word.lower()
        i += 1
    return answer
    