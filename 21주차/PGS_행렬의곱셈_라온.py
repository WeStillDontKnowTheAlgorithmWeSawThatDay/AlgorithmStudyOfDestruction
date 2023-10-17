import copy

def calculate(row1, row2):
    n = len(row1)
    result = 0
    for i in range(n):
        result += (row1[i] * row2[i])
    return result

def solution(arr1, arr2):
    temp = [[0] * len(arr2) for _ in arr2[0]]
    for i, arr in enumerate(arr2):
        for j, n in enumerate(arr):
            temp[j][i] = n
    arr2 = copy.deepcopy(temp)
    
    row, column = len(arr1), len(arr2)
    answer = [[0]*column for _ in range(row)]
    
    for i in range(row):
        for j in range(column):
            answer[i][j] = calculate(arr1[i], arr2[j])
    return answer

# 뒤집는 방법
# new_list = list(map(list, zip(*mylist)))
