def solution(s, n):
    answer = ''
    
    for char in s:
        if (char == ' '):
            answer += ' '
        else:
            code = ord(char)
            newNumber = code + n
            if(97 <= code and code <= 122):
                if(122 < newNumber):
                    answer += chr(newNumber - 26)
                else:
                    answer += chr(newNumber)
            else:
                if(90 < newNumber):
                    answer += chr(newNumber - 26)
                else:
                    answer += chr(newNumber)
    return answer