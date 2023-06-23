def solution(numbers):
    answer = ''
    tem = []
    
    for num in numbers:
        tem.append(str(num))
    
    tem.sort(key = lambda x : x*4, reverse = True)
    
    return ''.join(tem)
# 93.3점 ㅠㅠ
