def solution(s, n):
    answer = ''
    for w in list(s):
        if w == " ":
            answer += w
            
        elif 'A' <= w <= 'Z':
            answer += chr(ord('A') + (ord(w) - ord('A') + n) % 26)
        
        elif 'a' <= w <= 'z':
            answer += chr(ord('a') + (ord(w) - ord('a') + n) % 26)
        
    return answer
