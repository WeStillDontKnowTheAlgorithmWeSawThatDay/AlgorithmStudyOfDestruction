N = int(input())
liquid = list(map(int, input().split()))

nowMin = 2000000000
ansList = []

le, ri = 0, N - 1

while le < ri:
    sumLiquid = liquid[le] + liquid[ri]
    # print(liquid[le], liquid[ri])
    if abs(sumLiquid) == nowMin:
        ansList.append([liquid[le], liquid[ri]])
        le += 1
        ri -= 1
        continue
    if abs(sumLiquid) < nowMin:
        nowMin = abs(sumLiquid)
        ansList = [[liquid[le], liquid[ri]]]
    if sumLiquid > 0:
        ri -= 1
    else:
        le += 1

print(*ansList[0])

# 이분탐색인가?
