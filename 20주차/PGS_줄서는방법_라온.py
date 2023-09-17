from itertools import permutations

def func(n, k):
    total = 1
    for i in range(n):
        total *= i+1
    divider = total // n
    quot, remain = k // divider, k % divider
    if remain != 0:
        quot += 1
    return quot, remain

def solution(n, k):
    answer = []
    origin_numbers = [i+1 for i in range(n)]
    origin_n = n
    while n >= 3:
        first, k = func(n, k)
        n -= 1
        target = origin_numbers[first-1]
        answer.append(target)
        origin_numbers.remove(target)
    
    numbers = []
    for i in range(1, origin_n+1):
        if i not in answer:
            numbers.append(i)
    answer+= list(permutations(numbers, len(numbers)))[k-1]     
    return answer
