def to_binary(s):
    n = 0
    while pow(2, n) <= s:
        n += 1
    binary_str = ''
    for i in range(n-1, -1, -1):
        if s - pow(2, i) >= 0:
            s -= pow(2, i)
            binary_str += '1'
        else:
            binary_str += '0'
    return binary_str
    
def solution(s):
    answer = [0, 0]

    while True:
        length = 0
        if s == '1':
            break
        for ch in s:
            if ch == '0':
                length += 1
        s = to_binary(len(s)-length)
        answer[0] += 1
        answer[1] += length
    return answer
