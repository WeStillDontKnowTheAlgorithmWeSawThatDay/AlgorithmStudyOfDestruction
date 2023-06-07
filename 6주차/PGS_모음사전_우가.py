from itertools import product

def solution(word):
    answer = []
    
    for i in range(1, 6):
        a = product(["A","E","I","O","U"], repeat = i)
        for aa in a:
            answer.append("".join(aa))
            
    answer.sort()

    return answer.index(word) + 1
