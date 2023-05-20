def solution(s):
    if len(s) == 4 or len(s) == 6:
        for i in s:
            if not i.isdigit():
                return False
        return True
    return False
