def solution(phoneBook):
    p = sorted(phoneBook)

    for a, b in zip(p, p[1:]):
        if b.startswith(a):
            return False
    return True
