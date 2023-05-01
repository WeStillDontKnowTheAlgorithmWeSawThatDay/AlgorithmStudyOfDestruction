def solution(numbers: list):
    result = list()
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if i != j and numbers[i] + numbers[j] not in result:
                print("exe")
                result.append(numbers[i] + numbers[j])
    result.sort()
    return result