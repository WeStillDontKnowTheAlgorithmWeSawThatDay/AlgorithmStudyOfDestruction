
def solution(strings, n):
    return sorted(strings, key=lambda string: (string[n], string))
