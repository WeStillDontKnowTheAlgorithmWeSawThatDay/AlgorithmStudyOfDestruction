import math

N = int(input())
AList = list(map(int, input().split()))
B, C = map(int, input().split())

cnt = len(AList)

for i in range(len(AList)):
    # print(AList[i] - B, C, (math.ceil((AList[i] - B) / C)))
    tmp = math.ceil((AList[i] - B) / C)
    if tmp < 0:
        tmp = 0
    cnt += tmp

# print(AList)

print(cnt)
