def solution(numbers, hand):
    clx = 0
    cly = 3
    crx = 2
    cry = 3
    answer = ''
    for n in numbers :
        ty, tx = find(n)
        if n == 1 or n == 4 or n == 7 :
            answer += "L"
            cly, clx = ty, tx
            continue
        if n == 3 or n == 6 or n == 9 :
            answer += "R"
            cry, crx = ty, tx
            continue
        dl = abs(clx - tx) + abs(cly - ty)
        dr = abs(crx - tx) + abs(cry - ty)
        if dl > dr :
            cry, crx = ty, tx
            answer += "R"
            continue
        if dl < dr :
            cly, clx = ty, tx
            answer += "L"
            continue
        if hand == "left" :
            cly, clx = ty, tx
            answer += "L"
        else :
            cry, crx = ty, tx
            answer += "R"

    return answer

def find(n):
    if n == 1 :
        return 0, 0
    if n == 2 :
        return 0, 1
    if n == 3 :
        return 0, 2
    if n == 4 :
        return 1, 0
    if n == 5 :
        return 1, 1
    if n == 6 :
        return 1, 2
    if n == 7 :
        return 2, 0
    if n == 8 :
        return 2, 1
    if n == 9 :
        return 2, 2
    if n == 0 :
        return 3, 1
