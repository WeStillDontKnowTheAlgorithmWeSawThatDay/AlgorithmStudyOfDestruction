import sys  ## 이거 안하면 시간초과뜸;;; 문제 잘못골랐다 이것도

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    arr = []
    for _ in range(N):
        arr.append(list(map(int, input().split())))
    # print(arr)

    arr.sort(key=lambda x: x[0])
    # print(arr)
    cnt = 1
    passRank = arr[0][1]
    for i in range(1, N):
        if arr[i][1] < passRank:
            passRank = arr[i][1]
            cnt += 1

    print(cnt)
