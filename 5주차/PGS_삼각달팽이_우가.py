def solution(n):
    answer = []
    
    arr = [[0 for _ in range(n)] for _ in range(n)]
    
    색칠 = n + (n * n - n) // 2

    cnt = 1
    count = 0
    
    while count != 색칠:
        
        for i in range(count, n):
            if arr[i][count] > 0:
                continue
            arr[i][count] = arr[i-1][count] + 1
            cnt += 1
        for i in range(count, n - count):
            if arr[n - 1 - count][i] > 0:
                continue
            arr[n - 1 - count][i] = arr[n - 1 - count][i-1] + 1
            cnt += 1
        for i in range(n - 1, count, -1):
            if arr[i][i - count] > 0:
                continue
            arr[i][i - count] = arr[i + 1][i + 1 - count] + 1
            cnt += 1
        count += 1
    
    for i in range(n):
        for j in range(n):
            if arr[i][j] > 0:
                answer.append(arr[i][j])
    
    return answer
