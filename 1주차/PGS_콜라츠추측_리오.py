def solution(num):
    c = 0
    while num != 1 and c <= 500 :
        if num % 2 == 0 :
            num /= 2
            c += 1
            continue
        num = num*3 +1
        c += 1
    answer = c
    if c == 501 :
        answer = -1
    return answer
