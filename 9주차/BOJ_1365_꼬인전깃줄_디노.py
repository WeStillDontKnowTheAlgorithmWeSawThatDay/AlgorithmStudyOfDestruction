import bisect

N = int(input())
line = list(map(int, input().split()))

dp = []
cnt = 0

for num in line:
    if len(dp) == 0:
        dp.append(num)
        cnt += 1
        continue

    if dp[-1] < num:
        dp.append(num)
        cnt += 1
    else:
        dp[bisect.bisect_left(dp, num)] = num

print(N - cnt)

# 가장 긴 증가하는 부분 수열 문제랑 똑같음
# bisect_left -> 해당 값이 처음 나온 인덱스
# bisect_right -> 해당 값이 마지막으로 나온 인덱스 + 1

#        0  1  2  3  4  5  6  7
# arr = [1, 2, 3, 3, 3, 4, 5, 6]
# print(bisect.bisect_left(arr, 3))   # 2
# print(bisect.bisect_right(arr, 3))  # 5
