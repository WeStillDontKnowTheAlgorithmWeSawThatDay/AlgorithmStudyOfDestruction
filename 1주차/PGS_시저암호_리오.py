def solution(s, n):
    l = []
    for c in list(s) :
        if c == ' ' :
            l.append(' ')
        if c.isupper() :
            l.append(chr((ord(c) + n - ord('A')) % 26 + ord('A')))
        if c.islower() :
            l.append(chr((ord(c) + n - ord('a')) % 26 + ord('a')))

    answer = ''.join(l)
    return answer

print(solution("AB", 1))
