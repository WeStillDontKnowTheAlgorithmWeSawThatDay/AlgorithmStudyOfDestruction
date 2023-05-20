def solution(s):
    l = list(s)

    if len(l) != 4 and len(l) != 6 :
        return False

    for x in l :
        if not x.isdigit() :
            return False

    return True
