
def cut(n, s):
    strings = ""
    before = s[0:n]
    i, num = 0, 0
    while i < len(s):
        if s[i:i+n] == before:
            num += 1
        else:
            # strings += s[i-n:i] if num == 1 else (str(num) + s[i-n:i])
            if num == 1:
                strings += s[i-n:i]
            else:
                strings += (str(num) + s[i-n:i])
            before = s[i:i+n]
            num = 1
        i += n
    if num == 1:
        strings += s[i-n:i]
    else:
        strings += (str(num) + s[i-n:i])
    return len(strings)

def solution(s):
    answer = 1000
    for i in range(len(s)):
        answer = min(answer, cut(i+1, s))
    return answer

''' 이전 풀이
def func(string_list):
    num = 0
    remain = []
    temp = 0 # 10 넘는지 확인하는 용도
    for idx, data in enumerate(string_list):
        if idx == len(string_list)-1:
            remain.append(data)
            break
        if data == string_list[idx+1]:
            if temp == 0 or temp == 8: 
                num += 1
            temp += 1
        else: 
            temp = 0
            remain.append(data)
    return num + len(''.join(remain))
    
def solution(s):
    answer = 0
    length = []
    for i in range(1,len(s)+1): # 자르는 단위
        j = 0
        string = ''
        string_list = []
        while j < len(s): # 문자열 길이
            string_list.append(s[j: j+i])
            j = j + i
        
        string = '/'.join(string_list)
        length.append(func(string_list))
        
    answer = min(length)
    return answer
'''