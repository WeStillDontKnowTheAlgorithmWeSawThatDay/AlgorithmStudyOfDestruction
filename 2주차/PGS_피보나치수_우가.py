def solution(n):
    arr = []
    arr.append(0)
    arr.append(1)
    arr.append(1)

    for i in range(1, n - 1):
        arr.append(arr[i] + arr[i+1])

    return arr[n] % 1234567

