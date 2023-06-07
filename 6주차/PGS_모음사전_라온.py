def solution(word):
    answer = 0
    orders = {
        "A": 0,
        "E": 1,
        "I": 2,
        "O": 3,
        "U": 4
    }
    words = list(word)
    num = 4
    temp = 0
    for word in words:
        n = num
        while(n >= 0):
            temp += 5**n
            n -= 1
        answer += (temp*orders[word])
        temp = 0
        num -= 1
        answer += 1
    return answer
    