# 답지 보았다. 어렵다 
def solution(name):
    answer = 0
    for n in name:
        if n == "A":    continue
        answer += min(abs((ord('Z') - ord(n))+1),  abs(ord('A') - ord(n)))
    
    length = len(name)
    move = length - 1
    for i, n in enumerate(name):    
        pos = i + 1
        while pos < length and name[pos] == 'A':
            pos += 1
        move = min(move, 2*i + (length-pos), 2*(length-pos) + i)
    return answer + move
    