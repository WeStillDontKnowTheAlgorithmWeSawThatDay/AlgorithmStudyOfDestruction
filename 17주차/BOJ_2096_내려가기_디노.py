N = int(input())
arr = list(map(int, input().split()))

maxDP = arr
minDP = arr

for _ in range(N - 1):
    arr = list(map(int, input().split()))
    maxDP = [arr[0] + max(maxDP[0], maxDP[1]), arr[1] + max(maxDP), arr[2] + max(maxDP[1], maxDP[2])]
    minDP = [arr[0] + min(minDP[0], minDP[1]), arr[1] + min(minDP), arr[2] + min(minDP[1], minDP[2])]

print(max(maxDP), min(minDP))


# arr = [list(map(int, input().split())) for _ in range(N)]
#
# stack = [[0, 0, arr[0][0]], [0, 1, arr[0][1]], [0, 2, arr[0][2]]]
#
# ansList = []
# while stack:
#     x, y, cnt = stack.pop()
#     if x == N - 1:
#         ansList.append(cnt)
#         continue
#     if y == 0:
#         stack.append([x + 1, 0, cnt + arr[x + 1][0]])
#         stack.append([x + 1, 1, cnt + arr[x + 1][1]])
#     if y == 1:
#         stack.append([x + 1, 0, cnt + arr[x + 1][0]])
#         stack.append([x + 1, 1, cnt + arr[x + 1][1]])
#         stack.append([x + 1, 2, cnt + arr[x + 1][2]])
#     if y == 2:
#         stack.append([x + 1, 1, cnt + arr[x + 1][1]])
#         stack.append([x + 1, 2, cnt + arr[x + 1][2]])
#
# print(max(ansList), min(ansList))
