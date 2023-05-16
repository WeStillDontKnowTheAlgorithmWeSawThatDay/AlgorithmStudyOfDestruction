def solution(s):

    b = []
    a = list(s.split(" "))
    
    if len(s) == 1 and s[0] == '':
        return ''
    
    if s[0] == ' ' and len(s) == 1:
        return ' '
    
    for st in a:
        answer = ''
        for i in range(len(st)):
            if i % 2 == 0:
                answer += st[i].upper()
            else:
                answer += st[i].lower()

        b.append(answer)
    
    return ' '.join(b)

# gpt가 품
def solution(s):
    return ' '.join([''.join([st[i].upper() if i % 2 == 0 else st[i].lower() for i in range(len(st))]) for st in s.split(' ')])
