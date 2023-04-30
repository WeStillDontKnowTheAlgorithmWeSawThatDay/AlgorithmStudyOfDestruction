def solution(s, n):
    low = "abcdefghijklmnopqrstuvwxyz"
    up = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    answer = ""
    for target in s:
        if target in low:
            index = low.find(target) + n
            answer += low[index%26]
        elif target in up:
            index = up.find(target)+n
            answer += up[index%26]
        else:
            answer += " "
    return answer
print(solution("a B z E", 4))
