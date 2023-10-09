def solution(arr1, arr2):
    answer = []

    for i in range(len(arr1)):
        tmp = []
        for j in range(len(arr2[0])):
            num = 0
            for y in range(len(arr2)):
                # print(arr1[i][y], arr2[y][j])
                num += arr1[i][y] * arr2[y][j]
            # print(num)
            tmp.append(num)
        answer.append(tmp)

    return answer
