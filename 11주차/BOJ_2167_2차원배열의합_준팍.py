import sys

input = sys.stdin.readline

N, M = map(int, input().split())

# 2차원 배열 만들기
prefix_sum = [[0] * (M + 1) for _ in range(N + 1)]

# 2차원 배열 초기화
for i in range(1, N + 1):
    row = list(map(int, input().split()))
    for j in range(1, M + 1):
        # 2차원 배열에 누적합 넣기
        prefix_sum[i][j] = prefix_sum[i-1][j] + prefix_sum[i][j-1] - prefix_sum[i-1][j-1] + row[j-1]

K = int(input())
for _ in range(K):
    i, j, x, y = map(int, input().split())
    # 누적합 구하기
    result = prefix_sum[x][y] - prefix_sum[i-1][y] - prefix_sum[x][j-1] + prefix_sum[i-1][j-1]
    print(result)
