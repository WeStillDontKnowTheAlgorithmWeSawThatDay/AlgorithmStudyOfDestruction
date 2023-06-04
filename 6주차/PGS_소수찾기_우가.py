from itertools import permutations


def solution(numbers):
    answer = 0
    
    d = set()
    for _ in range(1, len(numbers) + 1):
        a = permutations(numbers, _)
        for bb in list(a):
            c = "".join(bb)
            e = int(c)
            if e != 0:
                d.add(e)
                
    for dd in d:
        if checkPri(dd):
            answer += 1
    
    return answer

def checkPri(number):
    if number < 2:
        return False
    for i in range(2, number + 1):
        cccc = number % i
        if cccc == 0 and number != i:
            return False
        if cccc == 0 and number == i:
            return True
