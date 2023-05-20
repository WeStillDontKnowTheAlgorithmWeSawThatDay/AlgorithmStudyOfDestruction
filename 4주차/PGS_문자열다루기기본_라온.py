def solution(s):
    if len(s) != 4 and len(s) != 6:
        return False
    for i in s:
        if i < '0' or i > '9':
            return False
    return True
