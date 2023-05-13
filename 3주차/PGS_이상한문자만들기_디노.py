def solution(s):
    answer = []
    words = list(s.split(" "))
    for w in words:
        c_word = ''
        for i in range(len(w)):
            if i % 2 == 0:
                c_word += w[i].upper()
            else:
                c_word += w[i].lower()
        answer.append(c_word)
    return ' '.join(answer)
