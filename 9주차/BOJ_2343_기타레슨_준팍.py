import sys

input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))

# 블루레이의 최소 크기는 강의 길이 중 최대 값 이상이어야 한다. 
# (강의 길이보다 블루레이의 크기가 작으면 블루레이에 담을 수 없는 강의가 생기기 때문에)
# 블루레이의 최대 크기는 강의의 총 길이와 같다.
# (블루레이의 갯수가 하나인 경우 한 블루레이에 모든 영상을 담아야 하기 때문에)
start, end = max(arr), sum(arr)

while start <= end:
    mid = (start + end) // 2
    count = 1
    temp_sum = 0

    for i in range(N):
        if temp_sum + arr[i] > mid:
            temp_sum = 0
            count += 1
        temp_sum += arr[i]

    if count <= M:
        end = mid - 1
    else:
        start = mid + 1

print(start)
