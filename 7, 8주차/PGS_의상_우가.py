def solution(clothes):
    answer = 1
    a = {}
    
    for cloth in clothes:
        a[cloth[1]] = []
    
    for cloth in clothes:
        a[cloth[1]].append(cloth[0])
    
    for aa in a:
        answer *= (len(a[aa]) + 1)
    
    return answer - 1

print(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]))
