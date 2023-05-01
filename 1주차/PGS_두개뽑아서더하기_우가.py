def solution(numbers):
    sets = set([])

    for i in range(0, len(numbers) - 1):
        for j in range(i + 1, len(numbers)):
            sets.add(numbers[i] + numbers[j])
    
    lsss = list(sets)
    
    return sorted(lsss)